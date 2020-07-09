
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


                   

