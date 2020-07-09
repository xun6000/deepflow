import csv
result = []
towrite=[]
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
with open('./three_records/threshold/soft.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        [a,b,c]=(row[0].split(",")[0:3])
        #print(a)
        #print(b)

        try:
            a = float(a)
            b = float(b)
            c = float(c)
            result.append([a,b,c])
        except:
            print("done")
            break


with open('./three_records/val_fold_1.lst', 'r') as f:
    content = f.readlines()
content = [x.strip().split("\t") for x in content]
#print(len(content))
count =0
p=0
g=0
folder = content[0][2].split("/")
print(folder)
if folder[3] == "CellCycle":
    pre_patient=content[0][2].split("/")[5]
else:
    pre_patient = content[0][2].split("/")[6]
#print(content)
#print(len(content))
thld=0.35
ans = []
total=0
for i in range(len(content)):
    if content[i][2].split("/")[3] == "CellCycle":
        current_patient = content[i][2].split("/")[5]
    else:
        current_patient = content[i][2].split("/")[6]
    if "third" in content[i][2]:
        print(i)
        break
    #print(current_patient,pre_patient)
    if current_patient==pre_patient:
        if result[i][0]<result[i][2] and result[i][1]<result[i][2]:
            #print(result[i])
            continue
        if result[i][0]>result[i][1] :
            #print("hrere")

            g+=1
        elif result[i][0]<result[i][1]:



            p += 1
    else:
        print(pre_patient,",",g*1.0/(g+p),g,p)
        towrite.append(str(pre_patient)+","+str(g*1.0/(g+p)))
        total+=g+p
        if g*1.0/(g+p)>thld:
            #print(g,p)
            ans.append(((pre_patient), "good",g,p))
        else:
            #print(g, p)
            ans.append(((pre_patient), "poor",g,p))
        pre_patient=current_patient
        if result[i][0] < result[i][2] and result[i][1] < result[i][2]:
            g = 0
            p = 0
        elif result[i][0] > result[i][1]:

            g =1
            p=0
        elif result[i][0] < result[i][1]:
            g=0
            p =1
# print(pre_patient,",",g*1.0/(g+p))
# towrite.append(str(pre_patient)+","+str(g*1.0/(g+p)))
# total+=g+p
print("total si ",ans)
# if g*1.0/(g+p)>thld:
#     #print(g,p)
#     ans.append(((pre_patient),"good"))
# else:
#     #print(g, p)
#     ans.append(((pre_patient),"poor"))

hehe = []
for i in ans:

    if i[0]!="873_s1":
        hehe.append((int(i[0][1:]),i[1]))
hehe.sort()
for i in hehe:
    print(i)





