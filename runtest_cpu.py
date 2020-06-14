# pylint: skip-file
import sys, os
import mxnet as mx
import numpy as np
import logging
import errno

#setup logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG)

#device specification
num_cpus = 2
#num_gpus = 4
cpus = [mx.cpu(i) for i in [num_cpus]]
#gpus = [mx.gpu(i) for i in range(num_gpus)]

kv = mx.kvstore.create('local_allreduce_device')

#define hyperparameters
num_epoch = 100
batch_size = 20
learning_rate = 0.0005
weight_decay = 0.01
factor_epoch = 10
lr_factor = 0.25
#model output path
model_prefix = 'model/dual'

def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

"""Define model architecture
"""

def _SimpleConvFactory(data, num_filter, kernel, stride=(1,1), pad=(0, 0), act_type="relu"):
    conv = mx.symbol.Convolution(data=data, num_filter=num_filter, kernel=kernel, stride=stride, pad=pad)
    bn = mx.symbol.BatchNorm(data=conv)
    act = mx.symbol.Activation(data = bn, act_type=act_type)
    return act

def _DualDownsampleFactory(data, ch_3x3):
    # conv 3x3
    conv = _SimpleConvFactory(data=data, kernel=(3, 3), stride=(2, 2), num_filter=ch_3x3, pad=(1, 1))
    # pool
    pool = mx.symbol.Pooling(data=data, kernel=(3, 3), stride=(2, 2),pad=(1, 1), pool_type='max')
    # concat
    concat = mx.symbol.Concat(*[conv, pool])
    return concat

def _DualFactory(data, ch_1x1, ch_3x3):
    # 1x1
    conv1x1 = _SimpleConvFactory(data=data, kernel=(1, 1), pad=(0, 0), num_filter=ch_1x1)
    # 3x3
    conv3x3 = _SimpleConvFactory(data=data, kernel=(3, 3), pad=(1, 1), num_filter=ch_3x3)
    #concat
    concat = mx.symbol.Concat(*[conv1x1, conv3x3])
    return concat

data = mx.symbol.Variable(name="data")
conv1 = _SimpleConvFactory(data=data, kernel=(3,3),  pad=(1,1), num_filter=96, act_type="relu")
in3a = _DualFactory(conv1, 32, 32)
in3b = _DualFactory(in3a, 32, 48)
in3c = _DualDownsampleFactory(in3b, 80)
in4a = _DualFactory(in3c, 112, 48)
in4b = _DualFactory(in4a, 96, 64)
in4c = _DualFactory(in4b, 80, 80)
in4d = _DualFactory(in4c, 48, 96)
in4e = _DualDownsampleFactory(in4d, 96)
in5a = _DualFactory(in4e, 176, 160)
in5b = _DualFactory(in5a, 176, 160)
in6a = _DualDownsampleFactory(in5b, 96)
in6b = _DualFactory(in6a, 176, 160)
in6c = _DualFactory(in6b, 176, 160)
pool = mx.symbol.Pooling(data=in6c, pool_type="avg", kernel=(8,8), name="global_avg")
flatten = mx.symbol.Flatten(data=pool)
fc = mx.symbol.FullyConnected(data=flatten, num_hidden=2)
softmax = mx.symbol.Softmax(data=fc, name = "softmax")

def get_train_iter():
    """ creates train data iterator
    """
    train_dataiter = mx.io.ImageRecordIter(
            shuffle = True,
            path_imgrec="records/train_fold_1.rec",
            mean_img="records/ifc_mean.bin",
            rand_crop=True,
            rand_mirror=True,
            min_crop_size=64,
            max_crop_size=64,
            max_rotate_angle = 180,
            data_shape=(3,64,64),
            batch_size=batch_size,
            preprocess_threads=4)
    return train_dataiter

def get_test_iter():
    """ creates test data iterator
    """
    test_dataiter = mx.io.ImageRecordIter(
        path_imgrec="records/test_fold_1.rec",
        mean_img="records/ifc_mean.bin",
        rand_crop=False,
        rand_mirror=False,
        data_shape=(3,64,64),
        round_batch = False,
        batch_size=batch_size,
        preprocess_threads=4)
    return test_dataiter

def _file_len(fname):
    """ scans number of lines in file
    """
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def train_ifc():
    """ training routine to fit the model
    """

    # create new model with params
    model = mx.mod.Module(
        context       = cpus,
        symbol        = softmax
    )

    #define Xavier initialization
    initializer = mx.init.Xavier(rnd_type='gaussian', factor_type="in", magnitude=2.34)
    #batch
    batch_end_callbacks = [mx.callback.Speedometer(batch_size, 100)]

    #get number of steps for one epoch
    epoch_size = _file_len('records/train_fold_1.lst')//batch_size
    #define learning rate scheduler
    lr_scheduler = mx.lr_scheduler.FactorScheduler(
                step = max(int(epoch_size * factor_epoch), 1),
                factor = lr_factor)
    #define optimizer hyperparameter
    optimizer_params = {
            'learning_rate': learning_rate, 
            'wd' : weight_decay,
            'lr_scheduler' : lr_scheduler,
            }
    #optional plot routine for network architecture
    '''
    digraph = mx.viz.plot_network(softmax, shape={'data':(batch_size, 3, 64, 64)}, node_attrs={"fixedsize":"false"})
    digraph.view()
    '''
    #define checkpoint which saves model at the end of an epoch
    checkpoint = None if model_prefix is None else mx.callback.do_checkpoint(model_prefix)
    make_sure_path_exists(model_prefix.split('/')[0])

    #fit the model
    model.fit(get_train_iter(),
        begin_epoch        = 0,
        num_epoch          = num_epoch,
        eval_data          = get_test_iter(),
        eval_metric        = ['accuracy'],
        kvstore            = kv,
        optimizer          = "rmsprop",
        optimizer_params   = optimizer_params,
        initializer        = initializer,
        batch_end_callback = batch_end_callbacks,
        epoch_end_callback = checkpoint,
        allow_missing      = True,
        monitor            = None)
    print("Training completed!")

def predict(): 
   """ prediction routine which saves testset features and softmax outputs to disc
   """
   model = mx.model.FeedForward.load(model_prefix, num_epoch, ctx = cpus)  
   internals = softmax.get_internals()
   fea_symbol2 = internals["flatten0_output"]
   fea_symbol1 = internals["softmax_output"]
   group = mx.symbol.Group([fea_symbol1, fea_symbol2])
   feature_extractor = mx.model.FeedForward(ctx=cpus, symbol=group,
                                         arg_params=model.arg_params,
                                         aux_params=model.aux_params,
                                         allow_extra_params=True)
   out = feature_extractor.predict(get_test_iter())  
   np.savetxt("soft.csv", out[0], fmt='%.5f', delimiter=",")
   np.savetxt("features.csv", out[1], fmt='%.5f', delimiter=",")
   print("Prediction completed, outputs dumped!")
  

if __name__ == "__main__":
  print("start")
  #train_ifc()
  print("start to predict")
  predict()
  

