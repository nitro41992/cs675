import sys
import math
import random


# Read File
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
    data[i].append(1)
    i += 1

rows = len(data)
cols = len(data[0])
f.close()
# print(f'Data: {data}')
# print(f'rows: {rows}')
# print(f'cols: {cols}')

# Read Labels
label_data = sys.argv[2]
f = open(label_data)
labels = {}

l = f.readline()
while(l != ''):
    a = l.split()
    labels[int(a[1])] = int(a[0])
    if(labels[int(a[1])] == 0):
        labels[int(a[1])] = -1
    else:
        labels[int(a[1])] = 1
    l = f.readline()
f.close()

# print(data)
# print(labels)

# dot product function


def dot_product(refw, refx):
    dot_product = 0
    for j in range(0, cols, 1):
        dot_product += refw[j]*refx[j]
    return dot_product


# Initialize w
w = []
for j in range(0, cols, 1):
    w.append(float(0.02*random.uniform(0, 1) - 0.01))


# dellf descent iteration
eta = 0.001
diff = 1
error = 0
count = 0

# compute dellf and error
while (diff > 0.00000001):
    dellf = []
    dellf.extend(0 for _ in range(cols))

    for i in range(0, rows, 1):
        if (labels.get(i) != None):
            a = labels[i] * dot_product(w, data[i])
            for j in range(0, cols):
                if a < 1:
                    dellf[j] += -(labels[i] * data[i][j])
                else:
                    dellf[j] += 0

    # print(f'dellf: {dellf}')

    # update w
    for j in range(0, cols, 1):
        w[j] -= eta*dellf[j]
    # print(f'w[j]: {w[j]}')

    prevObj = error
    error = 0
    # compute error

    for i in range(0, rows, 1):
        if (labels.get(i) != None):
            error += max(0, 1 - (labels.get(i)) * dot_product(w, data[i]))

    diff = abs(prevObj - error)

    # print(f'diff: {diff}')
    # print("error: ", error)

print(f'w =  {w[0:2]}')
# distance from origin calculation (pythagorean theorem)
normw = 0
for j in range(0, cols-1, 1):
    normw += w[j]**2
print(f'w0 = {w[2]}')

normw = math.sqrt(normw)
origin_distance = abs(w[len(w)-1]/normw)
print('distance from origin =  ', origin_distance)

# prediction
for i in range(0, rows, 1):
    if (labels.get(i) == None):
        dp = dot_product(w, data[i])
        if dp > 0:
            print("1,", i)
        else:
            print("0,", i)
