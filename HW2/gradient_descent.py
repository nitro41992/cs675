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

n = []
n.append(0)
n.append(0)
l = f.readline()
while(l != ''):
    a = l.split()
    labels[int(a[1])] = int(a[0])
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
eta = 0.0001
stop = 0.001
error = 0

# compute dellf and error
while True:
    dellf = []
    dellf.extend(0 for _ in range(cols))
    prev_iter_error = error
    for i in range(0, rows, 1):
        if (labels.get(i) != None):
            dp = dot_product(w, data[i])
            for j in range(0, cols, 1):
                dellf[j] += float((labels[i]-dp)*data[i][j])

    # print(f'dellf: {dellf}')

    # update w
    for j in range(0, cols, 1):
        w[j] += eta*dellf[j]
    # print(f'w[j]: {w[j]}')

    # compute error
    error = 0
    for i in range(0, rows, 1):
        if (labels.get(i) != None):
            error += (labels[i] - dot_product(w, data[i]))**2

    # print("error: ", error)
    # print("prevError", prev_iter_error)
    # print("error diff", abs(prev_iter_error - error))

    if abs(prev_iter_error - error) <= stop:
        break


# distance from origin calculation
normw = 0
for j in range(0, cols-1, 1):
    normw += w[j]**2
    print(f'w: {abs(w[j])}')

normw = math.sqrt(normw)
origin_distance = abs(w[len(w)-1]/normw)
print('distance from origin: ', origin_distance)

# prediction
for i in range(0, rows, 1):
    if (labels.get(i) == None):
        dp = dot_product(w, data[i])
        if dp > 0:
            print("1,", i)
        else:
            print("0,", i)
