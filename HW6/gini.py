import sys
import random
import math

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


# Read Labels
label_data = sys.argv[2]
f = open(label_data)
labels = {}

l = f.readline()
while(l != ''):
    a = l.split()
    labels[int(a[1])] = int(a[0])
    l = f.readline()
f.close()


# Splitting
def split(thres, coln, dataset):
    left = list()
    right = list()

    for row in dataset:
        if row[coln] < thres:
            left.append(row)
        else:
            right.append(row)
    return left, right  # returns the 2 groups


predicted = list()
for r in range(len(data)):
    if (labels.get(r) != None):
        data[r].append(labels[r])
    else:
        predicted.append(data[r])
dataset = list()
for r in data:
    length = len(r)
    if length == len(data[0]):
        dataset.append(r)

col_label = len(dataset[0]) - 1

class_values = list(set(row[col_label] for row in dataset))
col_num = 0
row_num = 0
coord = 0
gini_value = 1
group_count = None
sim_count = 0

for col in range(len(dataset[0]) - 1):
    for row in range(len(dataset)):
        groups = split(dataset[row][col], col, dataset)
        left = groups[0]
        right = groups[1]
        tot_rows = len(left) + len(right)
        gini = 0.0

        # Calculate Gini Index
        for group in groups:
            size = len(group)
            if size == 0:
                continue
            prob = 1
            for class_val in class_values:
                p = [row[-1] for row in group].count(class_val) / size
                prob = prob * p
            gini += (prob) * (size / tot_rows)

        if gini < gini_value:
            col_num = col
            row_num = row
            coord = dataset[row][col]
            gini_value = gini
            group_count = groups
        elif gini == gini_value:
            sim_count = sim_count + 1

if (sim_count == ((len(dataset) * 2) - 1)):
    col_num = 0
    row_numVal = dataset[0][col_num]
    row_num = 0
    for row in range(len(dataset)):
        if dataset[row][col_num] > row_numVal:
            row_num = row
            row_numVal = dataset[row][col_num]
    coord = dataset[row_num][col_num]
    gini_value = gini
    group_count = split(dataset[row_num][col_num], col_num, dataset)

stump = {'column': col_num, 'row': row_num, 'value': coord,
         'groups': group_count, 'gini': gini_value}


win_col = list()
max = -9999
for r in range(len(dataset)):
    win_col.append(dataset[r][col_num])
win_col.sort()
for r in range(len(dataset)):
    val = dataset[r][col_num]
    if val < coord:
        if val > max:
            max = val

s = (max + coord) / 2

print('Column Number:', stump['column'])
print('Gini Value:', stump['gini'])
print('Split Value:', s)
