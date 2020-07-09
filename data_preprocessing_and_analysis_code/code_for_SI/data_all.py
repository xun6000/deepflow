
base = 0

import random
import os

count = 0

train_good = []
val = []
test = []
train_poor = []
count = 0
folders = os.listdir("all/CellCycle/good")
for i in range(len(folders)):
    if folders[i] == ".DS_Store":
        continue

    subfolder = os.listdir("all/CellCycle/good/" + folders[i])
    for k in range(len(subfolder)):
        if subfolder[k] == ".DS_Store":
            continue

        a = random.random()

        if a < 0.8:
            train_good.append(
                str(count) + "\t0\t" + "../data/CellCycle/all/CellCycle/good" + "/" + folders[i] + "/" + subfolder[
                    k] + "\n")
            count += 1
        else:
            val.append(
                str(count) + "\t0\t" + "../data/CellCycle/all/CellCycle/good" + "/" + folders[i] + "/" + subfolder[
                    k] + "\n")
            count += 1

folders = os.listdir("all/CellCycle/poor")
for i in range(len(folders)):
    if folders[i] == ".DS_Store":
        continue

    subfolder = os.listdir("all/CellCycle/poor/" + folders[i])
    for k in range(len(subfolder)):
        if subfolder[k] == ".DS_Store":
            continue
        a = random.random()
        if a < 0.8 and folders[i] not in ['9', '14', '1']:

            for m in range(4):
                train_poor.append(
                    str(count) + "\t1\t" + "../data/CellCycle/all/CellCycle/poor" + "/" + folders[i] + "/" + subfolder[
                        k] + "\n")
                count += 1
        else:
            for m in range(4):
                val.append(
                    str(count) + "\t1\t" + "../data/CellCycle/all/CellCycle/poor" + "/" + folders[i] + "/" + subfolder[
                        k] + "\n")
                count += 1

folders = os.listdir("all_cana")  # this is incorrect
for i in range(len(folders)):
    if folders[i] == ".DS_Store":
        continue

    subfolder = os.listdir("all_cana/" + folders[i] + "/c")
    for k in range(len(subfolder)):
        if subfolder[k] == ".DS_Store":
            continue
        # poor in train

        else:
            if folders[i] in ["1", "2", "3", "4", "5", "22"]:  # poor noot in train
                # print("fefefe")
                test.append(
                    str(count) + "\t1\t" + "../data/CellCycle/all_cana" + "/" + folders[i] + "/c/" + subfolder[
                        k] + "\n")
                count += 1
            else:

                test.append(
                    str(count) + "\t0\t" + "../data/CellCycle/all_cana" + "/" + folders[i] + "/c/" + subfolder[
                        k] + "\n")
                count += 1

print(train_good)
print(train_poor)
print(test)
print(len(train_good))
print(len(train_poor))
print(len(test))
print(len(val))

train = train_good + train_poor

random.shuffle(train)

file = open("all_records/train_fold_1.lst", "w")

for ii in range(len(train)):
    file.write(train[ii])

file.close()

file = open("all_records/val_fold_1.lst", "w")

for ii in range(len(val)):
    file.write(val[ii])

file.close()

file = open("all_records/test_fold_1.lst", "w")

for ii in range(len(test)):
    file.write(test[ii])

file.close()

file = open("all_records/test_fold_1.txt", "w")

for ii in range(len(test)):
    file.write(test[ii])

file.close()
