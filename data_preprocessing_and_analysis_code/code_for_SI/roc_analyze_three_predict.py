import csv

result = []
towrite = []


third = 0
with open('./three_records/predict/soft.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        [a, b, c] = (row[0].split(",")[0:3])
        # print(a)
        # print(b)

        try:
            a = float(a)
            b = float(b)
            c = float(c)
            result.append([a, b, c])
        except:
            print("done")
            break

with open('./three_records/test_fold_1.lst', 'r') as f:
    content = f.readlines()
content = [x.strip().split("\t") for x in content]
# print(len(content))
count = 0
p = 0
g = 0
folder = content[0][2].split("/")
print(folder)
if folder[3] == "CellCycle":
    pre_patient = content[0][2].split("/")[5]
else:
    pre_patient = content[0][2].split("/")[4]
# print(content)
# print(len(content))
thld = 0.6
ans = []
total = 0
for i in range(len(content)):
    if content[i][2].split("/")[3] == "CellCycle":
        current_patient = content[i][2].split("/")[5]
    else:
        current_patient = content[i][2].split("/")[4]

    if current_patient == pre_patient:
        if result[i][0] < result[i][2] and result[i][1] < result[i][2]:
            third += 1
            continue
        if result[i][0] > result[i][1]:
            # print(current_patient,content[i][2].split("/")[6],"good")

            g += 1
        elif result[i][0] < result[i][1]:
            # print(current_patient,content[i][2].split("/")[6],"poor")



            p += 1
    else:
        print("patients", pre_patient, ",", g * 1.0 / (g + p), g, p, third)
        towrite.append(str(pre_patient) + "," + str(g * 1.0 / (g + p)))
        total += g + p
        if g * 1.0 / (g + p) > thld:
            # print(g,p)
            ans.append(((pre_patient), "good"))
        else:
            # print(g, p)
            ans.append(((pre_patient), "poor"))
        pre_patient = current_patient
        if result[i][0] < result[i][2] and result[i][1] < result[i][2]:

            g = 0
            p = 0
        elif result[i][0] > result[i][1]:

            g = 1
            p = 0
        elif result[i][0] < result[i][1]:
            g = 0
            p = 1
print(pre_patient, ",", g * 1.0 / (g + p))
towrite.append(str(pre_patient) + "," + str(g * 1.0 / (g + p)))
total += g + p
print("total si ", total)
if g * 1.0 / (g + p) > thld:
    # print(g,p)
    ans.append(((pre_patient), "good"))
else:
    # print(g, p)
    ans.append(((pre_patient), "poor"))

hehe = []
for i in ans:

    if i[0] != "873_s1":
        hehe.append((int(i[0]), i[1]))
hehe.sort()
for i in hehe:
    print(i)
