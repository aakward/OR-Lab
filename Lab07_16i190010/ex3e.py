#Code for ALG-LAB7
def distance(m,n):
        sum=0.0
        for i in range(len(m)):
                sum=sum+(m[i]-n[i])**2
        return sum

import numpy as np
import timeit
np.random.seed(1000) #for repeatability
N = 200
d = 5000 #Consider the dimension which caused failure in the previous experiment
lmbda = [1000,100,10,1,0.1,0.01,0.001]
eps = np.random.rand(N,1) #random noise
#Create data matrix, label vector
A = np.random.randn(N,d)
xorig = np.ones( (d,1) )
y = np.dot(A,xorig) + eps
#initialize the optimization variable to be used in the new algo ALG-LAB7
x = np.zeros((d,1))
epochs = 20 #initialize the number of rounds needed to process
t = 1.0
arr = np.arange(N) #index array
start = timeit.default_timer() #start the timer
for f in range(len(lmbda)):
    print "Running for Value of lambda=",lmbda[f]    
    for epoch in range(epochs):
        np.random.shuffle(arr) #shuffle every epoch
        for i in np.nditer(arr): #Pass through the data points
    # Update x using x <- x - 1/t * g_i (x)
            ss=0
            for m in range(d):
                ss=ss+(A[i][m]*x[m])              
            for j in range(d):
                x[j]=x[j]-(((ss-y[i])*A[i][j])+(lmbda[f]*x[j])/200.0)/t
            t = t+1.0
                
    alglab7time = timeit.default_timer() - start #time is in seconds
    x_alglab7 = x
    v=np.dot(A,x_alglab7)
    print "time taken: ",alglab7time
    print "||Ax_alglab7-y||^2= ",distance(y,v)
    print "||x_alglab7-xorig||^2= ",distance(x_alglab7,xorig)
#print the time taken, ||Ax_alglab7 - y||^2, ||x_alglab7 - xorig||^2