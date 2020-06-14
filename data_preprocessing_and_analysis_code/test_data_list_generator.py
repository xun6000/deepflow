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
path=["recheck/test_of_canada"]
writepath = []
# print(folder)
count = 10000

#newpath=["xuefeinewdata/64*64FILTER"]
train=[]
test=[]



poorlist = ["873","947","467","141","86","698","209","180","468"]
foldermother = os.listdir(path[0])
for kil in range(len(foldermother)):
    if foldermother[kil] == ".DS_Store":
        continue

    folder = os.listdir(path[0] + "/" + foldermother[kil]+"/c")
    #print(folder)
    for k in range(len(folder)):
        if folder[k] == ".DS_Store":
            continue




        if foldermother[kil] not in poorlist:
            test.append(
                    str(count) + "\t0\t" + "../data/CellCycle/redo/test_of_canada" + "/" + foldermother[kil]+"/"+"c/"+folder[k] +  "\n")  # 205

            count += 1
        else:
            test.append(
                str(count) + "\t1\t" + "../data/CellCycle/redo/test_of_canada" + "/" + foldermother[kil] + "/" + "c/" +
                folder[k] + "\n")  # 205
            count +=1










file = open("recheck/test_fold_1.lst", "w")
for ii in range(len(test)):
    file.write(test[ii])
file.close()

file = open("recheck/test_fold_1.txt", "w")

for ii in range(len(test)):
    file.write(test[ii])

file.close()

