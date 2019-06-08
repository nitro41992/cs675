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

# Initialize w
w=[]
prevW=[]
for i in range(0, cols, 1):
	prevW.append(float(2))
	w.append(float(0))
	w[i]=mean1[i]-mean0[i]


#####################################
###		compute until convergence
#####################################

sum=1
prevsum=0
print("while loop starting")


while(abs(sum-prevsum)>0.001):	

	delF=[] #start delF at 0 everytime we do an iteration.
	for i in range(0, cols, 1):
		delF.append(float(0)) ##as many columns, or dimensions of data, there are in the datapoints will be needed in delF

	for i in range(0, rows, 1):
		for j in range(0, cols, 1):
			dotprod=0
			for wcols in range(0, cols, 1):
				dotprod+=w[wcols]*data[i][wcols]
			delF[j]+= 2*(trainlabels.get(i) - dotprod)*data[i][j]

	for j in range(0, cols, 1):
			w[j]=w[j]+0.000000000000000001*float(delF[j])
	
	
	prevsum=sum
	sum=0
	for i in range(0, rows, 1):
		for j in range(0, cols, 1):
			dotprod=0;
			for wcols in range(0, 3 ,1):
				dotprod+=w[wcols]*data[i][wcols]
			sum+=(trainlabels.get(i)-dotprod)**2
	print("Sum is: " + str(sum) + " prevsum is: " + str(prevsum))
print("When using the stopping point of 0.001, w is: ")
print(w)
magnitude =0
for i in range(0, cols-1, 1):
	magnitude+= w[i]**2
magnitude=math.sqrt(magnitude)
print("The distance of plane to origin is about", abs(w[cols-1]/magnitude))


########################
### Classify unlabld points
##########################

print("classifying!\n\n\n\n")
testfile = sys.argv[3];
t = open(testfile);
test = []
l=t.readline()
output = open("testoutput.txt", "r+")
trow=0;
while(l != ''):
	a=l.split()
	l2=[]
	for j in range(0, len(a), 1):
		l2.append(int(a[j]))
	l2.append(1); #for the w0;
	sum=0
	for j in range(0, len(a), 1):
		sum+=w[j]*l2[j]; ##get the sum wTx+w0 = y.
	print(sum)
	if (sum>0):
		output.write(str(1) + " " + str(trow) + "\n")
	else:
		output.write(str(0) + " " + str(trow) + "\n")
	trow+=1
	test.append(l2)
	l=t.readline()

output.close()
t.close()
print("The columns used are as follows\n")
print(w)