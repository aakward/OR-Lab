import numpy as np
import matplotlib.pyplot as plt
np.random.seed(1000)


def compute_loss_E(w,x,y,c):
    s=0
    
    for j in range(len(w)):
        s=s+(w[j]*x[j])
    s=s*y
    if s>=-1:
        return max(0,1-s)**2
    else:
        return -1.0*c*s
    
    
def compute_objfnval(lmbda,data,labels,model_w):
    s=0
    L=0    
    for j in range(len(model_w)):
        s=s+model_w[j]**2
    s=s*lmbda/2.0
    for j in range(len(data)):     
        l= compute_loss_E(model_w,data[j],labels[j])
        L=L+l
    L=L/len(data)
    s=s+L
    return s
    
def compute_grad_loss_E(lmbda,x,y,model_w,c):
    grad=[]
    
    sum1=0    
    for j in range(len(model_w)):
        sum1=sum1+(model_w[j]*x[j])
    if(1-y*sum1>=0 and y*sum1>=-1):
        for j in range(len(model_w)):
            g=0
            g=(1.0*lmbda*model_w[j]/n)-((2.0/n)*(1-y*sum1)*y*model_w[j]*x[j])  
            grad.append(g)
    elif(1-y*sum1<0 and y*sum1>=-1):
        for j in range(len(model_w)):
            g=0
            g=1.0*lmbda*model_w[j]/n
            grad.append(g)
    elif(y*sum1<-1):
        for j in range(len(model_w)):
            g=0
            g=(1.0*lmbda*model_w[j]/n)-(1.0*c*y*x[j]/n)
            grad.append(g)
    return grad

def OPT1(data,label,lmbda, num_epochs,c):
    data=np.squeeze(data)
    t = 1.0
    #initialize w
    w=[]
    for j in range(len(data[0])):
        w.append(0)
    arr = np.arange(data.shape[0])    
    for epoch in range(num_epochs):
        np.random.shuffle(arr) #shuffle every epoch
        for i in np.nditer(arr): #Pass through the data points
            step = 1.0/t
            g_i=compute_grad_loss_E(lmbda,data[i],label[i],w,c)
            
            for j in range(len(data[0])):
                w[j] = w[j] - (step*g_i[j])
            t = t+1
    
    return w


from sklearn import datasets
digits=datasets.load_digits()
dataX=digits.images.reshape((len(digits.images),-1))
labelsY=digits.target

data=[]
label=[]
for i in range(len(dataX)):
    if labelsY[i]==1:
        data.append(dataX[i])
        label.append(1)
    if labelsY[i]==7:
        data.append(dataX[i])
        label.append(-1)

n=len(data)
ntraindata=int(0.8*n)

def predict(w,x):
    s=0
    for j in range(len(x)):
        s=s+(w[j]*x[j])
    if s>=0:
        return 1
    else:
        return -1
    
def compute_accuracy(datas,labels,w):
    corr=0.0    
    for j in range(len(datas)):
        s=predict(w,datas[j])
        if s==labels[j]:
            corr=corr+1.0
    accuracy=corr/len(datas)*100
    return accuracy
        
lambdas=[0.01,0.1,1]
c_set=[2,3,4]        


for lmbda in lambdas:
    for c in c_set: 
        print "For lambda=",lmbda,"and c=",c,":"
        train_acc=[]
        test_acc=[]
        for shuffle in range(5):
            train_d=[]
            train_l=[]
            test_d=[]
            test_l=[]
            p=np.random.choice(n, ntraindata, replace=False)
            for i in range(len(data)):
                if ((i in p)==True):
                    train_d.append(data[i])
                    train_l.append(label[i])
                else:
                    test_d.append(data[i])
                    test_l.append(label[i])
            num_epochs=50
            w=OPT1(train_d,train_l,lmbda, num_epochs,c)
            train_acc.append(compute_accuracy(train_d,train_l,w))
            test_acc.append(compute_accuracy(test_d,test_l,w))
        mean_tr_acc=np.mean(train_acc)
        mean_te_acc=np.mean(test_acc)
        sd_tr_acc=np.std(train_acc)
        sd_te_acc=np.std(test_acc)
        print "Mean Training Accuracy: ",mean_tr_acc
        print "Mean Test Accuracy: ",mean_te_acc
        print "Std. Dev. of Training Accuracy: ",sd_tr_acc
        print "Std. Dev. of Testing Accuracy: ",sd_te_acc
        
        
        


    