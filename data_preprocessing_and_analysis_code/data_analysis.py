import csv
result = []
with open('/Users/gy12/Desktop/notebooks/bioml/redo/0212second/testofcanada/direct_train_and_test2/soft.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        [a,b]=(row[0].split(",")[0:2]) # 0 is good, 1 is poor, a is possibility of good, b is possibility of poor. This file is a little big longer than test list file because of the batch size. The last few prediction can be ignored.
        try:
            a = float(a)
            b = float(b)
            result.append([a,b])
        except:
            print("done")
            break


with open('/Users/gy12/Desktop/notebooks/bioml/redo/0212second/testofcanada/recheck/test_fold_1.lst', 'r') as f:
    content = f.readlines()
content = [x.strip().split("\t") for x in content]
#print(len(content))
count =0
p=0
g=0
pre_patient=content[0][2].split("/")[5]
print((pre_patient))
thld=0.35
ans = []
total=0
for i in range(len(content)):
    current_patient = content[i][2].split("/")[5]
    if current_patient==pre_patient:

        if result[i][0]>result[i][1] :


            g+=1
        elif result[i][0]<result[i][1]:



            p += 1
    else:
        print(pre_patient,g*1.0/(g+p))
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
print(pre_patient,g*1.0/(g+p))
total+=g+p
print("total is ",total)
if g*1.0/(g+p)>thld:
    #print(g,p)
    ans.append("good"+pre_patient)
else:
    #print(g, p)
    ans.append("poor"+pre_patient)
print(ans)


