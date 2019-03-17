import sys
import math

datafile = sys.argv[1]
trainlables_file = sys.argv[2]
# labels = sys.argv[3]

f = open(datafile, "r")

data = []
i = 0
l = f.readline()

while (l != ''):
    a = l.split()
    l2 = []
    for j in range(0, len(a), 1):
        l2.append((float(a[j])))
    data.append(l2)
    l = f.readline()

rows = len(data)
cols = len(data[0])

m0 = [0 for _ in range(len(data))]
m1 = [0 for _ in range(len(data))]


f1 = open(trainlables_file, "r")
trainlabels = {}
n = []
n.append(0)
n.append(0)
l = f1.readline()
while(l != ''):
    a = l.split()
    trainlabels[int(a[1])] = int(a[0])
    l = f1.readline()
    n[int(a[0])] += 1


m0 = []
m1 = []
for _ in range(cols):
    m0.append(1)
for _ in range(cols):
    m1.append(1)

for i in range(rows):
    if(trainlabels.get(i) != None and trainlabels[i] == 0):
        for j in range(cols):
            m0[j] = m0[j] + data[i][j]
    if(trainlabels.get(i) != None and trainlabels[i] == 1):
        for j in range(cols):
            m1[j] = m1[j] + data[i][j]


for j in range(cols):
    m0[j] = m0[j]/(n[0])
    m1[j] = m1[j]/(n[1])

sd0 = []
sd1 = []

for _ in range(cols):
    sd0.append(0)
for _ in range(cols):
    sd1.append(0)

for i in range(rows):
    for j in range(cols):
        if(trainlabels.get(i) != None and trainlabels[i] == 0):
            sd0[j] = sd0[j] + (m0[j] - data[i][j])**2
        if(trainlabels.get(i) != None and trainlabels[i] == 1):
            sd1[j] = sd1[j] + (m1[j] - data[i][j])**2
    sd0[j] = (sd0[j]/(n[0]-1))**0.5
    sd1[j] = (sd1[j]/(n[1]-1))**0.5


save = open("predicted_labels", "w")

for i in range(rows):
    if(trainlabels.get(i) == None):
        d0 = 0
        d1 = 0
        for j in range(cols):
            d0 = d0 + (((m0[j] - data[i][j])/sd0[j])**2)
            d1 = d1 + (((m1[j] - data[i][j])/sd1[j])**2)
        if(d0 < d1):
            print("0", i)
            save.write("0 " + str(i) + "\n")
        else:
            print("1", i)
            save.write("1 " + str(i) + "\n")
save.close()
