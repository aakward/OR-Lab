from sklearn.datasets import load_digits
import numpy as np
import matplotlib.pyplot as plt
from random import uniform
import math

def evalf(A,x,y,lmbda):
        ye=np.matmul(A,x)
        err=[ye[i]-y[i] for i in range(len(y))]
        sum=0.0
        for i in range(len(y)):
                sum=sum+err[i]**2
        return 0.5*sum
        
def gradf(A,x,y,lmbda,N,d):
        grad=[]
        for j in range(d):
                sum1=0.0
                for i in range(N):
                        temp=[A[i][k]*x[k] for k in range(d)]
                        sum1=sum1+(A[i][j]*(sum(temp)-y[i]))
                grad.append(sum1)
        print "(Y)"
        return grad

def hessian(A,x,y):
    A=np.matrix(A)
    B=A.T
    value=B*A
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
        
    

def main():
  #  np.random.seed(1000)
    from sklearn.datasets import load_digits
    digits=load_digits()
    
    N = digits.data.shape[0] #Number of data points
    d = digits.data.shape[1] #Dimension of data points

    A=digits.data

    y=1.0*np.ones([A.shape[0],1])
    for i in range(digits.target.shape[0]):
        y[i]=digits.target[i]

        
    start=0*np.ones([A.shape[1],1])
    k=0
    x=[]
    m=[]
    for i in range(len(start)):
        x.append(start[i])
    m.append(start)
    H=hessian(A,x,y)
    print H
    H_inv=H.I
    grad=gradf(A,x,y)
    grad2=[grad[i]**2 for i in range(len(grad))]
    obj=[]
    while(math.sqrt(sum(grad2))>0.00000001):
        dir=[]
        grad=gradf(A,x,y)
        H_inv=H_inv.tolist()
        for i in range(len(grad)):
            temp=0
            for j in range(len(grad)):
                temp=temp+(H_inv[i][j]*grad[j])
            dir.append(-1*temp)
        H_inv=np.matrix(H_inv)
        grad2=[dir[i]**2 for i in range(len(dir))]
        xx=inner_minima(A,x,y,dir)
        x=xx
        xx=[]
        obj.append(evalf(A,x,y))
        print evalf(A,x,y)
        m.append(x)
        k=k+1
        if(abs(evalf(A,m[k],y)-evalf(A,m[k-1],y)))<0.00000000000001:
                    break
    print "Optimal solution is: ",x
    print "Minimum Value of the function is: ",evalf(A,x,y)
    print "No. of iterations required is: ",k
   # num1=[i for i in range(len(obj))]
    #plt.scatter(num1,obj)
#    plt.title("Plot of Objective value in each iteration")
 #   plt.xlabel("Iterations")
  #  plt.ylabel("Objective value")
   # plt.show()
    #plt.savefig("output_ex12a.png")
#    plt.clf()
 #   x1=[m[i][0] for i in range(len(m))]
  #  x2=[m[i][1] for i in range(len(m))]
   # num2=[i for i in range(len(m))]
    #plt.scatter(x1,x2)
#    plt.title("Plot of x[1] vs x[0]")
 #   plt.xlabel("x[0]")
  #  plt.ylabel("x[1]")
   # plt.show()
    #plt.savefig("output_ex12b.png")
    
main()
    
    


