import numpy as np
import math

def evalf(A,x,y,lmbda):
        ye=np.matmul(A,x)
        
        err=[ye[i]-y[i] for i in range(len(y))]
        sum=0.0
        for i in range(len(y)):
            sum=sum+err[i]**2
        for i in range(len(x)):
            sum=sum+lmbda*x[i]**2
        return 0.5*sum
        
def gradf(A,x,y,lmbda,N,d):
        grad=[]
        for j in range(d):
                sum1=0.0
                for i in range(N):
                        temp=[A[i][k]*x[k] for k in range(d)]
                        sum1=sum1+(A[i][j]*(sum(temp)-y[i]))
                grad.append(sum1+lmbda*x[j])
        print "(Y)"
        return grad

def hessf(A,x,y,lmbda):
    A=np.matrix(A)
    B=A.T
    value=B*A
    Id=[]
    for i in range(len(value)):
        temp=[]        
        for j in range(len(value)):
            if(i==j):
                temp.append(1)
            else:
                temp.append(0)
        Id.append(temp)
    Id=np.matrix(Id)
    Id=Id*lmbda
    value=value+Id
    return value

    
def inner_minima(A,x,b,dr,lmbda):
        x=np.squeeze(np.array(x))
        y=[]
        y1=[]
        l=x
        u=[]
        r=0.9
        lamb=1
        print len(x)
        print len(dr)
        
        for i in range(len(x)):
            y.append(x[i]+lamb*dr[i])
            y1.append(x[i])
        while(evalf(A,y,b,lmbda)<evalf(A,y1,b,lmbda)):
                lamb=lamb+1
                y=[]
                y1=[]
                for i in range(len(x)):
                    y.append(x[i]+lamb*dr[i])
                    y1.append(x[i]+(lamb-1)*dr[i])
        for i in range(len(x)):
           # l.append(x[i]-(lamb+1)*dr[i])
            u.append(x[i]+(lamb+1)*dr[i])
        count=0
        while(abs(evalf(A,l,b,lmbda)-evalf(A,u,b,lmbda))>10**(-15)):
                
                count=count+1
                o=[l[i]+(r*(u[i]-l[i])) for i in range(len(x))]
                a=[u[i]-(r*(u[i]-l[i])) for i in range(len(x))]
                if(evalf(A,a,b,lmbda)<evalf(A,o,b,lmbda)):
                        u=[]
                        for i in range(len(x)):
                            u.append(o[i])

                else:
                        l=[]
                        for i in range(len(x)):
                            l.append(a[i])
        return l
        print "count= ",count
        
    

np.random.seed(1000)
from sklearn.datasets import load_digits
digits=load_digits()
N = digits.data.shape[0] #Number of data points
d = digits.data.shape[1] #Dimension of data points
    
A=digits.data
#A_t=A.T
#B=np.matmul(A_t,A)
#print B
        
y=1.0*np.ones([A.shape[0],1])
for i in range(digits.target.shape[0]):
    y[i]=digits.target[i]

    
    
start=0*np.ones([A.shape[1],1])
    
    
lmbda=0.1
k=0
x1=[]
m=[]
for i in range(len(start)):
    x1.append(start[i])
m.append(start)
H=hessf(A,x1,y,lmbda)
H=np.matrix(H)
H_inv=H.I
grad=gradf(A,x1,y,lmbda,N,d)
grad2=[grad[i]**2 for i in range(len(grad))]
obj=[]
while(math.sqrt(sum(grad2))>0.0000000000000001):
    dir=[]
    grad=gradf(A,x1,y,lmbda,N,d)
    H_inv=H_inv.tolist()
    for i in range(len(grad)):
        temp=0
        for j in range(len(grad)):
            temp=temp+(H_inv[i][j]*grad[j])
        dir.append(-1*temp)
    H_inv=np.matrix(H_inv)
    grad2=[dir[i]**2 for i in range(len(dir))]
    xx=inner_minima(A,x1,y,dir,lmbda)
    x1=xx
    xx=[]
    obj.append(evalf(A,x1,y,lmbda))
    print evalf(A,x1,y,lmbda)
    m.append(x1)
    k=k+1
    if(abs(evalf(A,m[k],y,lmbda)-evalf(A,m[k-1],y,lmbda))<0.0000001):
        break
print "Optimal solution is: ",x1
print "Minimum Value of the function is: ",evalf(A,x1,y,lmbda)
print "No. of iterations required is: ",k

    
    
    