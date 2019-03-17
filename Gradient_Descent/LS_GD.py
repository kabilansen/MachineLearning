import sys
from random import random
import operator


def dotProd(mat1, mat2):
    dp = 0
    for i in range(len(mat1)):
        dp += mat1[i]*mat2[i]
    return dp


def toMatrixArray(textFile):
    linefromFile = textFile.readline()
    matrixArray = []
    while (linefromFile != ''):
        a = linefromFile.split()
        l2 = []
        for j in range(0, len(a), 1):
            l2.append((float(a[j])))
            if(j == len(a)-1):
                l2.append(float(1))
        matrixArray.append(l2)
        linefromFile = textFile.readline()
    return matrixArray


datafile_name = sys.argv[1]
labelsfile_name = sys.argv[2]


labels_file = open(labelsfile_name, "r")
data_file = open(datafile_name, "r")

trainlabel_matrix = toMatrixArray(labels_file)

f1 = open(labelsfile_name, "r")
trainlabels = {}
n = []
n.append(0)
n.append(0)
l = f1.readline()
while(l != ''):
    a = l.split()
    if(int(a[0]) == 0):
        trainlabels[int(a[1])] = -1
    else:
        trainlabels[int(a[1])] = int(a[0])
    l = f1.readline()
    n[int(a[0])] += 1

data_file_matrix = toMatrixArray(data_file)
trainlabel_matrix = trainlabels
# print(trainlabel_matrix)
for i in range(len(trainlabel_matrix)):
    if(trainlabel_matrix.get(i) == 0):
        trainlabel_matrix[i] = -1

cols = len(data_file_matrix[0])
rows = len(data_file_matrix)


w = [(0.02*random() - 0.01) for i in range(cols)]

# print(w)
eta = 0.0001

# print(trainlabel_matrix)

###########
# Dell f
##########
ddf=[]
def del_difference(delf, delf_old):
    for i in range(len(delf)):
        ddf.append(delf[i] - delf_old[i])
    return ddf
def modulo(ddf):
    modulo=0
    for i in range(len(ddf)):
        modulo += ddf[i]**2
    return modulo**0.5
delf = []
delf_old = []
error=0
for j in range(cols):
    delf.append(0.001)
    delf_old.append(0.01)

flag = 0
k=0
while(flag != 1):
    k+=1
    # print("Iterations(expected<1000): ", k)
    # ddf = del_difference(delf, delf_old)
    # eta = dotProd(w,ddf)/modulo(ddf)**2
    for i in range(rows):
        if(trainlabel_matrix.get(i) != None):
            dp = dotProd(w, data_file_matrix[i])
            for j in range(cols):
                delf_old[j] = delf[j]
                delf[j] += (trainlabel_matrix.get(i) -
dp)*data_file_matrix[i][j]
    for j in range(cols):
        w[j] += eta*delf[j]
    error=0
    for i in range(rows):
        if(trainlabel_matrix.get(i) != None):
            error += (trainlabel_matrix.get(i) - dotProd(w,
data_file_matrix[i]))**2
        if(error<0.01):
            eta = 0.000001
            if(error<0.001):
                eta = 0.0000001
                if(error<0.00001):
                    eta = 0.00000001
                    if(error < 0.0000001):
                        flag = 1

for i in range(rows):
    if(trainlabel_matrix.get(i) == None):
        x = dotProd(w, data_file_matrix[i])
        if(x>0):
            print("1 ", i)
        else:
            print("0 ", i)




