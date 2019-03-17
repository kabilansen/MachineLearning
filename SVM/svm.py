import sys
import random
import operator
#import msvcrt as m

def normalize(dataFile):
    max = []
    min = []
    new = []
    writeData = open("normalized", "w")
    for _ in range(len(dataFile[0])):
        max.append(0)
        min.append(0)
        new.append(1)
    for i in range(len(dataFile)):
        for j in range(len(dataFile[0])-1):
            if(dataFile[i][j]> max[j]):
                max[j] = dataFile[i][j]
            if(dataFile[i][j]< min[j]):
                min[j] = dataFile[i][j]
    for j in range(len(dataFile[0])-1):
        new[j] = max[j] - min[j]
    for i in range(len(dataFile)):
        for j in range(len(dataFile[0])-1):
            if(max[j]-min[j] != 0 ):
                dataFile[i][j] = (dataFile[i][j] - min[j])/(max[j] - min[j])
                writeData.write(str(dataFile[i][j]) + " ")
        writeData.write("\n")
    return max, min

def changeEta(eta, error):
    if(error<eta):
        eta=eta*0.1
        return eta
    else:
        return eta

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

labelsfile_name = sys.argv[2]
datafile_name = sys.argv[1]

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
normalize(data_file_matrix) #Important!!!
#m.getch()
# print(trainlabel_matrix)
for i in range(len(trainlabel_matrix)):
    if(trainlabel_matrix.get(i) == 0):
        trainlabel_matrix[i] = -1

cols = len(data_file_matrix[0])
rows = len(data_file_matrix)


w = [(0.02*random.uniform(0,1) - 0.01) for i in range(cols)]

# print(w)
eta = 0.01

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


prev_error = max(0,1-(trainlabel_matrix.get(i)*dotProd(w, data_file_matrix[i])))
flag = 0
k=0
while(flag != 1):
    k+=1
    delf= []
    for j in range(rows):
        delf.append(0)
    #############
    #Compute Hinge Loss
    ##############
    for i in range(rows):
        if(trainlabel_matrix.get(i) != None):
            dp = dotProd(w, data_file_matrix[i])
            ydp = trainlabel_matrix.get(i)*dp
            for j in range(cols):
                if(ydp>=1):
                    delf[j] += 0
                elif(ydp<1):
                    delf[j] += -(data_file_matrix[i][j]*trainlabel_matrix.get(i))

    for j in range(cols):
        w[j] -= eta*delf[j]
    error = 0
    for i in range(rows):
        if(trainlabel_matrix.get(i) != None):
            ydp = trainlabel_matrix.get(i)*dp
            error += max(0,1-(trainlabel_matrix.get(i)*dotProd(w, data_file_matrix[i])))# hinge risk
            eta = changeEta(eta, abs(prev_error - error))


    #print(k, error, eta)
    if(abs(prev_error - error) < 0.000000001):
        flag = 1
        #print(w)
    prev_error = error
        # eta = changeEta(eta, error)

for i in range(rows):
    if(trainlabel_matrix.get(i) == None):
        x = dotProd(w, data_file_matrix[i])
        if(x>0):
            print("1 ", i)
        else:
            print("0 ", i)

