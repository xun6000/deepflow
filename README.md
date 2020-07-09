# Reconstructing cell cycle and disease progression using deep learning
This code contains the neural network implementation from the nature communication publication https://doi.org/10.1038/s41467-017-00623-3 . We use this network for our TNBC paper.

## Access the data
The data zip file is inside "data" folder, make sure to unzip and keep the folder structure as same as is as same as train_fold_1.lst and test_fold_1.lst.

## Running the code.
To reproduce the results from the publication, change the PATH2MXNET variable in generate_record_files.sh to your mxnet home folder and run:

```
sh generate_record_files.sh
```

Run the neural network training & prediction:

```
python3.5 run.py
```
or

```
python3.5 runtest_cpu.py
```


You need to run the code twice to reproduce the result. 
First time, train_fold_1.lst and test_fold_1.lst are the data in Cellcycle, the "test" data are the 20% data that are used to find out the threshold. After you make the prediction, you analyze the soft.csv to find a good threshold. 
Second time, change the test_fold_1.lst to another test_fold_1.lst which is another patient and make the prediction. 

## System Requirements
The results were generated with python3.5 on an Linux Red Hat 4.8.5-36.

Environments:
* GCC/5.4.0 CUDA/7.5.18 OpenMPI/1.10.3 Python/3.5.2

mxnet should be aligned with your CUDA vesion. 


Additional dependencies:
* mxnet 1.1.0 
* numpy 1.12.0
* cv2   3.4.1.15 


If you use google cloud deep learning service, which has cuda90, you can use :

pip3 install opencv-python==3.4.1.15 

pip3 install mxnet-cu90==1.1.0







The data folder contains data used for maintext.

The data for SI is in dropbox.
https://www.dropbox.com/sh/a7ef9987ez3aacf/AAAWl2cw-z8tKnprsWVhR5gSa?dl=0
You can find there are similarity in the file name which indicate they are a pair of training and test.

The folder data_preprocessing_and_analysis_code contains the code for data pre-processing and post analysis. The subfolder contains the code for SI.



