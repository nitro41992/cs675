import sys
import math
import random

from sklearn import svm
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.svm import LinearSVC
from sklearn.datasets import make_classification
from sklearn.model_selection import cross_val_score


data_file = sys.argv[1]
f = open(data_file, 'r')

data = []
i = 0
l = f.readline()
while(l != ''):
    a = l.split()
    l2 = []
    for j in range(0, len(a), 1):
        l2.append(a[j])
    data.append(l2)
    i = i+1
    l = f.readline()

rows = len(data)
cols = len(data[0])

train_label_file = sys.argv[2]
f = open(train_label_file, 'r')

train_labels = {}
i = 0
l = f.readline()

while(l != ''):
    a = l.split()
    if(int(a[0]) == 0):
        train_labels[int(a[1])] = int(a[0])-1
    else:
        train_labels[int(a[1])] = int(a[0])
    l = f.readline()


label_list = []
for label in train_labels:
    label_list.append(train_labels.get(label))


def dot_product(w, data):
    sum_dp = 0
    for j in range(0, cols, 1):
        sum_dp = sum_dp + w[j]*float(data[j])
    return sum_dp


def fixdata(data):
    new_data = []
    n = 0
    for row in data:
        if n in train_labels:
            new_data.append(row)
        n += 1
    return new_data


newdata_train = []
filename = sys.argv[3]
f = open(filename, 'w')


planes = [10, 100, 1000]  # , 10000]

for k in planes:
    print("For ", k, " random planes")
    for i in range(0, k, 1):

        list_train = []

        w = []
        for j in range(0, cols, 1):
            w.append(0)

        for j in range(0, cols, 1):
            w[j] = w[j] + random.uniform(1, -1)

        for i in range(0, rows, 1):
            dp = 0
            dp = dot_product(w, data[i])
            sign = int(math.copysign(1, dp))
            val = int((1+sign)/2)

            list_train.append(val)

        newdata_train.append(list_train)

        newdata_train_t = zip(*newdata_train)
        traindata = []
        for row in newdata_train_t:
            traindata.append(row)

    clf = svm.SVC(kernel='linear', C=.01, max_iter=10000)
    scores = cross_val_score(clf, fixdata(traindata), label_list, cv=5)
    scores[:] = [1-x for x in scores]
    scores_o = cross_val_score(clf, fixdata(data), label_list, cv=5)
    scores_o[:] = [1-x for x in scores_o]

    print("error for the new features: ", scores)
    print("mean error for the new features: ", scores.mean())
    print("error for eht orginal: ", scores_o)
    print("mean error for the orginal: ", scores_o.mean())

    f.write("error for the new features: " + "\n")
    f.write(str(scores)+"\n")
    f.write("mean error for the new features: " + "\n")
    f.write(str(scores.mean()) + "\n")

    f.write(" error for the original: " + "\n")
    f.write(str(scores_o) + "\n")
    f.write("mean error for the orginal: " + "\n")
    f.write(str(scores_o.mean()) + "\n")


f.close()
