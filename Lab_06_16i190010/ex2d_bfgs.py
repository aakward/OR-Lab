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
        while(abs(evalf(A,l,b,lmbda)-evalf(A,u,b,lmbda))>10**(-10)):
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
    Z=A*x_bar
    Z=np.squeeze(np.array(Z))
    y=[]
    for i in range(100):
        y.append(Z[i]+e[i])
    y=(np.squeeze(y)).tolist()
    start=[-5,-5]
    lmbda_v=[0.001,0.01,0.1,1,10,100,1000]
    itern=[]
    obj=[]
    for lmbda in lmbda_v:
        k=0
        x=[]
        m=[]
        for i in range(len(start)):
            x.append(start[i])
        m.append(start)
        H=hessian(A,x,y,lmbda)
        H_inv=H.I
        grad=gradf(A,x,y,lmbda)
        grad2=[grad[i]**2 for i in range(len(grad))]
        B=[]
        for i in range(2):
            temp=[]
            for j in range(2):
                if(i==j):
                    temp.append(1)
                else:
                    temp.append(0)
            B.append(temp)
        grad=gradf(A,x,y,lmbda)
        m_grad=[]
        m_grad.append(grad)
        grad2=[grad[i]**2 for i in range(len(grad))]
        
        while(math.sqrt(sum(grad2))>0.001):
                grad=np.matrix(grad)                
                B=np.matrix(B)
                B_inv=B.I
                B_inv=-B_inv
                grad=grad.T
                dir=B_inv*grad
                dir=np.squeeze(dir.tolist())
                xx=inner_minima(A,x,y,dir,lmbda)
                x=xx
                xx=[]
                
                print evalf(A,x,y,lmbda)
                m.append(x)
                grad=gradf(A,x,y,lmbda)
                grad2=[grad[i]**2 for i in range(len(grad))]
                grad=grad.tolist()                
                m_grad.append(grad)
                k=k+1
                s_k=[]
                y_k=[]
                for i in range(len(x)):
                        s_k.append(m[k][i]-m[k-1][i])
                        y_k.append(m_grad[k][i]-m[k-1][i])
                s1=0
                s2=0
                s_k=np.matrix(s_k)
                y_k=np.matrix(y_k)
                s_k_t=s_k.T
                y_k_t=y_k.T
                s1=s_k*B*s_k_t
                s2=y_k_t*y_k
                temp1=B*s_k_t*s_k*B
                temp2=y_k*y_k_t
                temp3=-temp1/s1
                temp4=temp2/s2
                B=B+temp3+temp4
                if(abs(evalf(A,m[k],y,lmbda)-evalf(A,m[k-1],y,lmbda))<0.000000000001):
                    break
        obj.append(evalf(A,x,y,lmbda))
        itern.append(k)
    print "No. of iterations reqd. for each lambda: ",itern
    minm=obj[0]
    best_lambda=0
    for i in range (len(obj)):
        if(obj[i]<=minm):
            minm=obj[i]
            best_lambda=lmbda_v[i]
    print "Minimum objective Value is: ",minm," corresponding to the value of lambda: ",best_lambda

    plt.scatter(lmbda_v,obj)
    plt.title("Plot of Objective value for different Lambda")
    plt.xlabel("Lambda")
    plt.ylabel("Objective Value")
    plt.show()
    plt.savefig("output_ex24_bfgs")
    

main()