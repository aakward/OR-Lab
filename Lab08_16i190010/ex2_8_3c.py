import numpy as np
import matplotlib.pyplot as plt
#np.random.seed(1000)
def compute_loss_h(w,x,y):
    s=0
    for j in range(len(w)):
        s=s+(w[j]*x[j])
    s=s*y[0]
    p=1-s
    if p>=0:    
        return p**2
    else:
        return 0


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
    q=compute_loss_h(model_w,x,y)
    if(q==0):
        for j in range(d):
            g=lmbda*model_w[j]/n
            grad.append(g)
    else:
        for j in range(d):
            g=(lmbda*model_w[j]/float(n))+((-2.0/n)*(y*x[j])*math.sqrt(q))
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
    accuracy=corr/len(data)*100.0
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
    acc_values_train=[]    
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
            ep_acc=compute_accuracy(data,label,w)
            acc_values_train.append(ep_acc)
    
    
    return acc_values_train
     
     
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
colour=['red','yellow','green','blue']
for i1 in range(len(lmbda_set)):
    train_acc=0
    train_acc= OPT1(train_data,train_label,lmbda_set[i1],num_epochs)
    plt.plot(train_acc,color=colour[i1])

plt.title("Training Data Accuracy in different epochs for different lambdas for squared hinge loss")
plt.xlabel("Epochs")
plt.ylabel("Training Data Accuracy")
plt.legend(["lambda=0.001","lambda=0.1","lambda=1","lambda=10"],loc='upper right')
plt.show()



        
        