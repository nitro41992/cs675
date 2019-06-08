import sys
import math


#Read File
datafile = sys.argv[1]
f = open(datafile)
data = []
i = 0
l = f.readline()

while (l != ''):
    a = l.split()
    l2 = []
    for j in range(0, len(a), 1):
        l2.append(float(a[j]))
    data.append(l2)
    l = f.readline()
rows = len(data)
cols = len(data[0])
f.close()

#Read Labels
labelfile = sys.argv[2]
f = open(labelfile)
trainlabels = {}

n = []
n.append(0)
n.append(0)
l = f.readline()
while(l != ''):
    a = l.split()
    trainlabels[int(a[1])] = int(a[0])
    l = f.readline()
    n[int(a[0])] += 1


#Compute Mean
mean0 = []
for j in range(0, cols, 1):
    mean0.append(1)
mean1 = []
for j in range(0, cols, 1):
    mean1.append(1)


for i in range(0, rows, 1):
    if (trainlabels.get(i) != None) and (trainlabels[i] == 0):
        for j in range(0, cols, 1):
            mean0[j] += data[i][j]
    if (trainlabels.get(i) != None) and (trainlabels[i] == 1):
        for j in range(0, cols, 1):
            mean1[j] += data[i][j]
for j in range(0, cols, 1):
    mean0[j] /= n[0]
    mean1[j] /= n[1]

#Compute Standard Deviation for Naive Bayes
stdev0 = []
for j in range(0, cols, 1):
    stdev0.append(1)

stdev1 = []
for j in range(0, cols, 1):
    stdev1.append(1)

for i in range(rows):
    if (trainlabels.get(i) != None) and (trainlabels[i] == 0):
        for j in range(cols):
            stdev0[j] += (data[i][j] - mean0[j])**2 
    if (trainlabels.get(i) != None) and (trainlabels[i] == 1):    
        for j in range(cols):
            stdev1[j] += (data[i][j] - mean1[j])**2
for j in range(cols):
    stdev0[j] = math.sqrt(stdev0[j] / n[0])
    stdev1[j] = math.sqrt(stdev1[j] / n[1])


#Classify Unlabeled Points Using Naive Bayes
for i in range(0, rows, 1):
    if trainlabels.get(i) == None:
        d0 = 0
        d1 = 0
        for j in range(0, cols, 1):
            d0 += ((mean0[j] - data[i][j]) / stdev0[j])**2
            d1 += ((mean1[j] - data[i][j]) / stdev1[j])**2
        if d0 < d1:
            print("0 ", i)
        else:
            print("1 ", i)