
base=0

import random
import os

path=["redo/CellCycle/good","redo/CellCycle/poor"]
writepath = []

count = 0
towritet = []

train=[]
test=[]
for pathnumber in range(2):

    folder = os.listdir(path[pathnumber])

    for k in range(len(folder)):
        if folder[k] == ".DS_Store":
            continue
        data = os.listdir(path[pathnumber]+"/"+folder[k])



        for i in range(len(data)):
            print(i)
            if data[i] == ".DS_Store":
               continue

            a = random.random()
            if a<0.80:
                if int(folder[k][1:]) >18:  # good
                    train.append(str(count)+"\t0\t"+"../data/CellCycle/"+path[pathnumber][5:]+ "/"+folder[k]+"/"+data[i]+"\n") #205
                else:  #poor
                    for m in range(4):
                        train.append(str(count) + "\t1\t" + "../data/CellCycle/"  +path[pathnumber][5:]+ "/"+folder[k] + "/" + data[i] + "\n")  # 205
            else:
                if int(folder[k][1:]) >18:
                    test.append(str(count)+"\t0\t"+"../data/CellCycle/"+path[pathnumber][5:]+ "/"+folder[k]+"/"+data[i]+"\n") #205
                else:

                    test.append(str(count) + "\t1\t" + "../data/CellCycle/"  +path[pathnumber][5:]+ "/"+folder[k] + "/" + data[i] + "\n")  #


            count+=1




random.shuffle(train)

file = open("redo/train_fold_1.lst", "w")

for ii in range(len(train)):
    file.write(train[ii])

file.close()

file = open("redo/test_fold_1.lst", "w")

for ii in range(len(test)):
    file.write(test[ii])

file.close()

file = open("redo/test_fold_1.txt", "w")

for ii in range(len(test)):
    file.write(test[ii])

file.close()