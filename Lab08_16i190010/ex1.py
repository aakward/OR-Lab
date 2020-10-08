import numpy as np
#for the following statement to compile successfully, you need the scikit-learn package.
#You can install it using pip install -U scikit-learn or conda install scikit-learn
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

#Use the first 80% of indexarr to create the train data and the remaining 20% to create the test data

train_data=[]
train_label=[]
test_data=[]
test_label=[]
c=0
for i in indexarr:
    if(c<0.8*n):
        train_data.append(iris.data[i])
        train_label.append(iris.label[i])
        c=c+1
    else:
        test_data.append(iris.data[i])
        test_label.append(iris.label[i])

#train_data = ????
#train_label = ????
#test_data = ????
#test_label = ????

def predict(w,x):
    s=np.dot(w,x)
    if s>=0:
        return 1
    else:
        return -1

def compute_accuracy(data,labels,model_w):
    corr=0    
    for j in range(len(data)):
        s=predict(model_w,data[j])
        if s==labels[j]:
            corr=corr+1
    accuracy=corr/len(data)*100
    return accuracy

#Use predict function defined above
#return ???

