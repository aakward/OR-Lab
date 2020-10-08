import numpy as np
import matplotlib.pyplot as plt
from random import uniform
import math

def evalf(A,x,y):
    A=np.matrix(A)
    x=np.matrix(x)
    x=x.T
    value=0
    B=A*x
    B=np.squeeze(np.array(B))
    for i in range(len(B)):
        value=value+(B[i]-y[i])**2
    value=value/2
    return value
        
def gradf(A,x,y):
    A=np.matrix(A)
    B=A.T
    B=B*A
    x=np.matrix(x)
    x=x.T
    B=B*x
    y=np.matrix(y)
    y=y.T
    C=(A.T)*y
    value=B-C
    value=np.squeeze(np.array(value))
    return value

def hessian(A,x,y):
    A=np.matrix(A)
    B=A.T
    value=B*A
    return value
    
def inner_minima(A,x,b,d):
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
        while(evalf(A,y,b)<evalf(A,y1,b)):
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
        while(abs(evalf(A,l,b)-evalf(A,u,b))>10**(-15)):
                count=count+1
                o=[l[i]+(r*(u[i]-l[i])) for i in range(len(x))]
                a=[u[i]-(r*(u[i]-l[i])) for i in range(len(x))]
                if(evalf(A,a,b)<evalf(A,o,b)):
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
    k=0
    x=[]
    m=[]
    for i in range(len(start)):
        x.append(start[i])
    m.append(start)
    H=hessian(A,x,y)
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
    num1=[i for i in range(len(obj))]
    plt.scatter(num1,obj)
    plt.title("Plot of Objective value in each iteration")
    plt.xlabel("Iterations")
    plt.ylabel("Objective value")
    plt.show()
    plt.savefig("output_ex12a.png")
    plt.clf()
    x1=[m[i][0] for i in range(len(m))]
    x2=[m[i][1] for i in range(len(m))]
    num2=[i for i in range(len(m))]
    plt.scatter(x1,x2)
    plt.title("Plot of x[1] vs x[0]")
    plt.xlabel("x[0]")
    plt.ylabel("x[1]")
    plt.show()
    plt.savefig("output_ex12b.png")
    
main()
    
    