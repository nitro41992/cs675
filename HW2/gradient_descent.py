import sys
import math
import random


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
labels = sys.argv[2]
f = open(labels)
trainlabels = {}

n = []
n.append(0)
n.append(0)
l = f.readline()
while(l != ''):
    a = l.split()
    trainlabels[int(a[1])] = int(a[0])
    l = f.readline()
f.close()


# Initialize w
w=[]
for j in range(0,cols,1):
	w.append(float(0.02*random.random() - 0.01))	

#print(w)

#dot product function
def dot_product(refw,refx):
        dot_product=0
        for j in range(0,cols,1):
                dot_product += refw[j]*refx[j]
        return dot_product

#Initialize w
w=[]
for j in range(0,cols,1):
	w.append(float(0.02*random.random()- 0.01))	

#gradient descent iteration
eta=0.001
stop_condition=0.001
error=0

while True:
	prevobj=error
	#compute gradient and error
	gradient=[]
	error=0
	for i in range (0,rows,1):
		if (trainlabels.get(i) != None and trainlabels.get(i) == 0):
			dp=dot_product(w,data[i]);
			error += (trainlabels[i] - dp)**2
			for j in range (0,cols,1):
				gradient.append(float((trainlabels[i]-dp)*data[i][j]))
	
	if abs(prevobj-error)<=stop_condition:       
	        break 
	#update w
	for j in range (0,cols,1):
		w[j]=w[j]+eta*gradient[j]

#distance from origin calculation
print("w: ", end='')
normw=0
for j in range(0,cols-1,1):
	print(abs(w[j]),'', end='')
	normw += w[j]**2
print()

normw = math.sqrt(normw)
d_origin = abs(w[len(w)-1]/normw)
print("distance from origin: ",d_origin)

#prediction
for i in range(0,rows,1):
    if (trainlabels.get(i) == None):
        dp=0
        for j in range(0,cols,1):
            dp+=data[i][j]*w[j]
            
        if dp>0:
            print("1,",i)
        else:
            print("0,",i)
