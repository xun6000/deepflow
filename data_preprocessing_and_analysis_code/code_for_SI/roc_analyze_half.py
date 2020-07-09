import csv
result = []
towrite=[]
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
with open('./half/soft.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        [a,b]=(row[0].split(",")[0:2])
        #print(a)
        #print(b)

        try:
            a = float(a)
            b = float(b)
            result.append([a,b])
        except:
            print("done")
            break


with open('./half/test_fold_1.lst', 'r') as f:
    content = f.readlines()
content = [x.strip().split("\t") for x in content]
#print(len(content))
count =0
p=0
g=0
folder = content[0][2].split("/")
if folder[3] == "CellCycle":
    pre_patient=content[0][2].split("/")[5]
else:
    pre_patient = content[0][2].split("/")[4]
#print(content)
#print(len(content))
thld=0.35
ans = []
total=0
for i in range(len(content)):
    if content[i][2].split("/")[3] == "CellCycle":
        current_patient = content[i][2].split("/")[5]
    else:
        current_patient = content[i][2].split("/")[4]

    if current_patient==pre_patient:

        if result[i][0]>result[i][1] :


            g+=1
        elif result[i][0]<result[i][1]:



            p += 1
    else:
        print(pre_patient,",",g*1.0/(g+p))
        towrite.append(str(pre_patient)+","+str(g*1.0/(g+p)))
        total+=g+p
        if g*1.0/(g+p)>thld:
            #print(g,p)
            ans.append("good"+pre_patient)
        else:
            #print(g, p)
            ans.append("poor"+pre_patient)
        pre_patient=current_patient
        if result[i][0] > result[i][1]:

            g =1
            p=0
        elif result[i][0] < result[i][1]:
            g=0
            p =1
print(pre_patient,",",g*1.0/(g+p))
towrite.append(str(pre_patient)+","+str(g*1.0/(g+p)))
total+=g+p
print("total si ",total)
if g*1.0/(g+p)>thld:
    #print(g,p)
    ans.append("good"+pre_patient)
else:
    #print(g, p)
    ans.append("poor"+pre_patient)
print(ans)
for i in ans:
    print(i)


