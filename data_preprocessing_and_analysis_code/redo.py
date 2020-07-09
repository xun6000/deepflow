
base = 0


import scipy.misc


import os

from PIL import Image
import numpy as np

path = ["updated/good", "updated/poor"]

for _ in path:
    files = os.listdir(_)
    for name in files:
        if name == ".DS_Store":
            continue
        if "merge" in name:
            patientnumber = name.split("_")[0]
            try:
                os.mkdir("CellCycle/" + _[-4:] + "/" + patientnumber)
            except:
                pass
                patientnumber
            img = Image.open(_ + "/" + name);
            img = np.array(img)
            a, b, c = (img.shape)
            count = 0
            strke = 64
            for i in range(int(a / strke) - 2):
                for j in range(int(b / strke) - 2):
                    current = img[strke * i:strke + strke * i, strke * j:strke + strke * j]
                    print(current.shape)
                    name = "CellCycle/" + _[-4:] + "/" + patientnumber + "/" + str(count) + ".png"
                    print(name)
                    count_t_cell = 0
                    count_ai_cell = 0
                    for ii in range(strke):
                        for jj in range(strke):
                            if int(current[ii][jj][0]) > 150 and int(current[ii][jj][1]) > 150 and int(
                                    current[ii][jj][2]) > 150:
                                count_ai_cell += 1
                            if int(current[ii][jj][0]) - int(current[ii][jj][1]) > 150:
                                count_t_cell += 1
                    if count_ai_cell >= 900 and count_t_cell > 0:
                        scipy.misc.imsave(name, current)
                    count += 1


                    # print(patientnumber)

writepath = []

count = 0
towritet = []

train = []
test = []









# for pathnumber in range(2):
#
#     folder = os.listdir(path[pathnumber])
#
#     for k in range(len(folder)):
#         if folder[k] == ".DS_Store":
#             continue
#         data = os.listdir(path[pathnumber]+"/"+folder[k])
#         print(data)
#
#
#         for i in range(len(data)):
#             print(i)
#             if data[i] == ".DS_Store":
#                continue
#
#             a = random.random()
#             if int(folder[k])not in [21,35,39]:
#                 if int(folder[k]) >18 :
#                     train.append(str(count)+"\t0\t"+"../data/CellCycle/"+path[pathnumber][5:]+ "/"+folder[k]+"/"+data[i]+"\n") #205
#                 else:
#                     for m in range(4):
#                         train.append(str(count) + "\t1\t" + "../data/CellCycle/"  +path[pathnumber][5:]+ "/"+folder[k] + "/" + data[i] + "\n")  # 205
#             else:
#                 if int(folder[k]) >18:
#                     test.append(str(count)+"\t0\t"+"../data/CellCycle/"+path[pathnumber][5:]+ "/"+folder[k]+"/"+data[i]+"\n") #205
#                 else:
#
#                     test.append(str(count) + "\t1\t" + "../data/CellCycle/"  +path[pathnumber][5:]+ "/"+folder[k] + "/" + data[i] + "\n")  #
#
#
#             count+=1




# for i in range(len(towritet)):
#     a =  random.random()
#     if a<0.85:
#         train.append(towritet[i])
#     else:
#         test.append(towritet[i])


# random.shuffle(train)
#
# file = open("0821/train_fold_1.lst", "w")
#
# for ii in range(len(train)):
#     file.write(train[ii])
#
# file.close()
#
# file = open("0821/test_fold_1.lst", "w")
#
# for ii in range(len(test)):
#     file.write(test[ii])
#
# file.close()
