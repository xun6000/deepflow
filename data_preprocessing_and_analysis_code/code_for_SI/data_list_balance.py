import os
import random
base=0
import copy
import os
#shutil.move("P23_GY/good","CellCycle")
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

#data = os.listdir(path[0])
import scipy.misc




import shutil
import random
import os
#shutil.move("P23_GY/good","CellCycle")
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import numpy as np


# print(folder)
count = 0

train_good = []
test=[]
train_poor = []
count = 0
folders = os.listdir("CellCycle/good")
for i in range(len(folders)):
    if folders[i] == ".DS_Store":
        continue
    if folders[i] in ["P30", "P26", "P36", "P35", "P26", "P23"]:
        subfolder = os.listdir("CellCycle/good/"+ folders[i])
        for k in range(len(subfolder)):
            if subfolder[k] == ".DS_Store":
                continue


            train_good.append(str(count) + "\t0\t" + "../data/CellCycle/CellCycle/good" + "/" + folders[i]+"/"+subfolder[k] +  "\n")
            count +=1
    else:
        subfolder = os.listdir("CellCycle/good/" + folders[i])
        for k in range(len(subfolder)):
            if subfolder[k] == ".DS_Store":
                continue
            test.append(
                    str(count) + "\t0\t" + "../data/CellCycle/CellCycle/good" + "/" + folders[i] + "/" + subfolder[
                        k] + "\n")
            count += 1
folders = os.listdir("CellCycle/poor")
for i in range(len(folders)):
    if folders[i] == ".DS_Store":
        continue

    subfolder = os.listdir("CellCycle/poor/"+ folders[i])
    for k in range(len(subfolder)):
        if subfolder[k] == ".DS_Store":
            continue


        train_poor.append(str(count) + "\t1\t" + "../data/CellCycle/CellCycle/poor" + "/" + folders[i]+"/"+subfolder[k] +  "\n")
        count +=1




folders = os.listdir("test_of_canada")  # this is incorrect
for i in range(len(folders)):
    if folders[i] == ".DS_Store":
        continue

    subfolder = os.listdir("test_of_canada/"+ folders[i]+"/c")
    for k in range(len(subfolder)):
        if subfolder[k] == ".DS_Store":
            continue
        if folders[i] in ["873","947","467","141"]:  #poor in train
            train_poor.append(str(count) + "\t1\t" + "../data/CellCycle/test_of_canada" + "/" + folders[i]+"/c/"+subfolder[k] + "\n")
            count +=1
        else:
            if folders[i] in ["86","315"]: #poor noot in train
                #print("fefefe")
                test.append(
                        str(count) + "\t1\t" + "../data/CellCycle/test_of_canada" + "/" + folders[i] + "/c/" + subfolder[
                            k] + "\n")
                count += 1
            else:

                test.append(
                    str(count) + "\t0\t" + "../data/CellCycle/test_of_canada" + "/" + folders[i] + "/c/" + subfolder[
                        k] + "\n")
                count += 1

print(train_good)
print(train_poor)
print(test)
print(len(train_good))
print(len(train_poor))
print(len(test))

train = train_good+train_poor

random.shuffle(train)

file = open("train_fold_1.lst", "w")

for ii in range(len(train)):
    file.write(train[ii])

file.close()

file = open("test_fold_1.lst", "w")

for ii in range(len(test)):
    file.write(test[ii])

file.close()

file = open("test_fold_1.txt", "w")

for ii in range(len(test)):
    file.write(test[ii])

file.close()


