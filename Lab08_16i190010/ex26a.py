import numpy as np
import matplotlib.pyplot as plt
np.random.seed(1000)
def compute_loss_h(w,x,y):
    s=0
    
    for j in range(len(w)):
        s=s+(w[j]*x[j])
    s=s*y
    return max(0,1-s)


def compute_objfnval(lmbda,data,labels,model_w):
    s=0
    L=0    
    for j in range(d):
        s=s+model_w[j]**2
    s=s*lmbda/2.0
    for j in range(len(data)):     
        l= compute_loss_h(model_w,data[j],y[j])
        L=L+l
    L=L/n
    s=s+L
    return s
    
def compute_grad_loss_h(lmbda,x,y,model_w):
    grad=[]
    
    sum1=0    
    for j in range(d):
        sum1=sum1+(model_w[j]*x[j])
    if(1-y*sum1<=0):
        for j in range(d):
            g=lmbda*model_w[j]/n
            grad.append(g)
    else:
        for j in range(d):
            g=(lmbda*model_w[j]/n)-(y*x[j]/n)
            grad.append(g)
    return grad

def predict(w,x):
    s=0
    for j in range(d):
        s=s+(w[j]*x[j])
    if s>=0:
        return 1
    else:
        return -1
    
def compute_accuracy(data,labels,model_w):
    corr=0.0    
    for j in range(len(data)):
        s=predict(model_w,data[j])
        if s==labels[j]:
            corr=corr+1.0
    accuracy=corr/len(data)*100
    return accuracy
    
    
        
def OPT1(data,label,lmbda, num_epochs):
    data=np.squeeze(data)
    t = 1.0
    #initialize w
    w2=[]
    w=[]
    for j in range(d):
        w.append(0)
    #w = ???
    arr = np.arange(data.shape[0])
    obj_values=[]    
  #  print len(data)
    for epoch in range(num_epochs):
        np.random.shuffle(arr) #shuffle every epoch
        for i in np.nditer(arr): #Pass through the data points
            step = 1.0/t
            g_i=compute_grad_loss_h(lmbda,data[i],label[i],w)
            
            for j in range(d):
                w[j] = w[j] - (step*g_i[j])
            t = t+1
            
            
        if epoch%10==0:
            ep_obj=compute_objfnval(lmbda,data,label,w)
            obj_values.append(ep_obj)
            #w2.append(w)
            #ep_acc=compute_accuracy(data,label,w)
            #acc_values_train.append(ep_acc)
    #plt.plot(acc_values_train)
    
    return obj_values
     
     
w1=[]   #for storing the interim values of w  
from sklearn.datasets import load_iris
iris = load_iris()
#check the shape of iris data
print(iris.data.shape)
A = iris.data
#check the shape of iris target
print(iris.target.shape)
#How many labels does iris data have?
#C=num_of_classes
#print(C)
n = iris.data.shape[0] #Number of data points
d = iris.data.shape[1] #Dimension of data points
#In the following code, we create a nx1 vector of target labels
y = 1.0*np.ones([A.shape[0],1])
for i in range(iris.target.shape[0]):
    if iris.target[i]==1:    
        y[i] =1 # Convert the classes 2,3,...,C to -1
    else:
        y[i]=-1
#Create an index array
indexarr = np.arange(n) #index array
np.random.shuffle(indexarr) #shuffle the indices

num_epochs=input("Enter the no. of epochs: ")
#Use the first 80% of indexarr to create the train data and the remaining 20% to create the test data

train_data=[]
train_label=[]
test_data=[]
test_label=[]
c=0

for i in indexarr:
    if(c<=0.8*n):
        train_data.append(iris.data[i])
        train_label.append(y[i])
        c=c+1
    else:
        test_data.append(iris.data[i])
        test_label.append(y[i])
lmbda_set=[0.001,0.1,1,10]
objective_values=[]
colour=['red','yellow','green','blue']
for i1 in range(len(lmbda_set)):
    obj_val_set= OPT1(train_data,train_label,lmbda_set[i1],num_epochs)
    objective_values.append(obj_val_set)
    plt.plot(objective_values[i1],color=colour[i1])

plt.title("Objective function in different epochs for different lambdas for hinge loss")
plt.xlabel("Epochs")
plt.ylabel("function value")
plt.legend(["lambda=0.001","lambda=0.1","lambda=1","lambda=10"],loc='upper right')
plt.show()



        
        