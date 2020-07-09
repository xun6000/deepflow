import combine
import cutw
import cutr
import os
import shutil
f = "D:/redo/quarter/three_cana"
d = os.listdir(f)
print(d)

for i in range(len(d)):
    new = os.listdir(f+"/"+d[i])
    for j in new:
        if j != "c":
            if "png" not in j and "jpg" not in j:
                shutil.rmtree(f + "/" + d[i] + "/" + j)
            else:
                os.remove(f + "/" + d[i] + "/" + j)

