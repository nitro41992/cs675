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

rows = len(data)
cols = len(data[0])
f.close()


# Read Labels
labels = {}
f = open(sys.argv[2])
l = f.readline()
class_count = []
class_count.extend(0 for _ in range(cols))

while (l != ''):
    a = l.split()
    labels[int(a[1])] = int(a[0])
    class_count[int(a[0])] = class_count[int(a[0])] + 1
    l = f.readline()
f.close()

gini_values = []
split_count = 0
l3 = [0, 0]
for j in range(0, cols, 1):
    gini_values.append(l3)
temp = 0
col = 0

for j in range(0, cols, 1):

    list_col = [item[j] for item in data]
    keys = sorted(range(len(list_col)), key=lambda k: list_col[k])
    list_col.sort()

    curr_gini = []
    prev_gini = 0
    for k in range(1, rows, 1):

        lsize = k
        rsize = rows - k
        lp = 0
        rp = 0

        for l in range(0, k, 1):
            if (labels[keys[l]] == 0):
                lp += 1
        for r in range(k, rows, 1):
            if (labels[keys[r]] == 0):
                rp += 1

        gini_index = (lsize / rows) * (lp / lsize) * (1 - lp / lsize) + \
            (rsize / rows) * (rp / rsize) * (1 - rp / rsize)

        curr_gini.append(gini_index)

        prev_gini = min(curr_gini)

        if (curr_gini[k - 1] == float(prev_gini)):
            gini_values[j][0] = curr_gini[k - 1]
            gini_values[j][1] = k

    if (j == 0):
        temp = gini_values[j][0]

    if (gini_values[j][0] <= temp):
        temp = gini_values[j][0]
        col = j
        split_count = gini_values[j][1]

        if (split_count != 0):
            split_count = (list_col[split_count] +
                           list_col[split_count - 1]) / 2
print("gini index:", temp, "columns:", col, "split count:", split_count)
