import combine_rvw
import cutw_rvw
import cutr_rvw
import os
f = "D:/redo/quarter/three_cana"
d = os.listdir(f)
print(d)

for i in range(len(d)):

    newname = f+"/"+d[i]
    cutw_rvw.cal(newname)
    print("cancer is ready")
    cutr_rvw.cal(newname)
    print("t cell is ready")
    combine_rvw.cal(newname)
    print("combine is ready")
