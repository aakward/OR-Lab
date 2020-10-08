import numpy as np
import matplotlib.pyplot as plt
from random import uniform
import math

def evalf(A,x,y,lmbda):
    A=np.matrix(A)
    x=np.matrix(x)
    x=x.T
    value=0
    B=A*x
    B=np.squeeze(np.array(B))
    for i in range(len(B)):
        value=value+(B[i]-y[i])**2
    inn=x.T*x
    value=value+(lmbda*inn)
    value=value/2
    value=np.squeeze(np.array(value))
    return value
        
def gradf(A,x,y,lmbda):
    A=np.matrix(A)
    B=A.T
    B=B*A
    x=np.matrix(x)
    x=x.T
    B=B*x
    D=lmbda*x
    y=np.matrix(y)
    y=y.T
    C=(A.T)*y
    value=B-C+D
    value=np.squeeze(np.array(value))
    return value

def hessian(A,x,y,lmbda):
    A=np.matrix(A)
    B=A.T
    value=B*A
    I=[]
    for i in range(len(value)):
        temp=[]        
        for j in range(len(value)):
            if(i==j):
                temp.append(1)
            else:
                temp.append(0)
        I.append(temp)
    I=np.matrix(I)
    I=I*lmbda
    value=value+I
    return value
    
def inner_minima(A,x,b,d,lmbda):
        x=np.squeeze(np.array(x))
        y=[]
        y1=[]
        l=x
        u=[]
        r=0.9
        lamb=1
        for i in range(len(x)):
            y.append(x[i]+lamb*d[i])
            y1.append(x[i])
        while(evalf(A,y,b,lmbda)<evalf(A,y1,b,lmbda)):
                lamb=lamb+1
                y=[]
                y1=[]
                for i in range(len(x)):
                    y.append(x[i]+lamb*d[i])
                    y1.append(x[i]+(lamb-1)*d[i])
        for i in range(len(x)):
           # l.append(x[i]-(lamb+1)*d[i])
            u.append(x[i]+(lamb+1)*d[i])
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
    np.random.seed(1000)
    A=np.random.randn(100,2)

    x_bar=[uniform(1,5),uniform(-5,-8)]
    e=np.random.randn(100,1)
    
    x_bar=np.matrix(x_bar)
    x_bar=x_bar.T
    B=A*x_bar
    B=np.squeeze(np.array(B))
    y=[]
    for i in range(100):
        y.append(B[i]+e[i])
    y=(np.squeeze(y)).tolist()
    start=[0,0]
    lmbda_v=[0.001,0.01,0.1,1,10,100,1000]
    itern=[]
    obj=[]
    for lmbda in lmbda_v:
        x=[]
        m=[]
        k=0
        for i in range(len(start)):
            x.append(start[i])
        m.append(start)
        H=hessian(A,x,y,lmbda)
        H_inv=H.I
        grad=gradf(A,x,y,lmbda)
        grad2=[grad[i]**2 for i in range(len(grad))]
        
        while(math.sqrt(sum(grad2))>0.0000000000000001):
            dir=[]
            grad=gradf(A,x,y,lmbda)
            H_inv=H_inv.tolist()
            for i in range(len(grad)):
                temp=0
                for j in range(len(grad)):
                    temp=temp+(H_inv[i][j]*grad[j])
                dir.append(-1*temp)
            H_inv=np.matrix(H_inv)
            grad2=[dir[i]**2 for i in range(len(dir))]
            xx=inner_minima(A,x,y,dir,lmbda)
            x=xx
            xx=[]
            print evalf(A,x,y,lmbda)
            m.append(x)
            k=k+1
            if(abs(evalf(A,m[k],y,lmbda)-evalf(A,m[k-1],y,lmbda))<0.00000000000001):
                    break
        obj.append(evalf(A,x,y,lmbda))
        itern.append(k)
    print "No. of iterations reqd for each lambda: ",itern
    minm=obj[0]
    best_lambda=0
    for i in range (len(obj)):
        if(obj[i]<=minm):
            minm=obj[i]
            best_lambda=lmbda_v[i]
    print "Minimum objective Value is: ",minm," corresponding to the value of lambda: ",best_lambda
#    print "Optimal solution is: ",x
 #   print "Minimum Value of the function is: ",evalf(A,x,y,lmbda)
  #  print "No. of iterations required is: ",k
   # num1=[i for i in range(len(obj))]
    plt.scatter(lmbda_v,obj)
    plt.title("Plot of Objective value for different Lambda")
    plt.xlabel("Lambda")
    plt.ylabel("Objective Value")
    plt.show()
    plt.savefig("output_ex24_newton")
    
    
main()
    
    