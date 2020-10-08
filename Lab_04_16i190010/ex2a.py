import math

import matplotlib.pyplot as plt
import numpy as np

val=[]
points=[]
iter=[]

def evalf(x):
    value=0
    for i in range(1000):
        value=value+(-40*x[i]+3)
    for i in range(999):
        value=value+((x[i]**2+x[999]**2)**2)
    return value

def gradf(x):
    g=[0 for i in range(len(x))]
    for i in range(len(x)-1):
        g[i]=-40+2*(x[i]**2+x[len(x)-1]**2)*2*x[i]
    g[len(x)-1]=-40
    for i in range(len(x)-1):
        g[len(x)-1]=g[len(x)-1]+(2*((x[i]**2)+(x[len(x)-1]**2)*2*x[len(x)-1]))
    return g

def inner_minima(x,d):
        y=x
        l=x
        r=0.9

        lamb=1
        b=[y[i]+lamb*d[i] for i in range(len(x))]
        while(evalf(b)<evalf(y)):
            lamb=lamb+1
            y=b
            b=[x[i]+lamb*d[i] for i in range(len(x))]
            print "yyyy"
        count=0
        while(abs(evalf(l)-evalf(b))>10**(-10)):

                count=count+1
                a=[r*l[i]+ (1-r)*b[i] for i in range(len(x))]
                v=[r*b[i]+ (1-r)*l[i] for i in range(len(x))]

                if(evalf(a)<evalf(v)):
                        b=v

                else:
                        l=a
                points.append(evalf(l))


        val.append(evalf(l))
        iter.append(count)
        return l
        print "count= ",count

def main():

    m=[]
    y=[2.15 for i in range(1000)]
    x=y
    k=0
    grad=gradf(y)
    grad2=[grad[i]**2 for i in range(1000)]
    while(math.sqrt(sum(grad2))>0.001):
        d=[]
        grad=gradf(y)

        grad2=[grad[i]**2 for i in range(1000)]
        d=[-grad[i] for i in range(1000)]
        xx=inner_minima(x,d)
        x=xx
        k=k+1
        m.append(xx)
        print xx[0]
        if(k>1):
            if(m[k-1]==m[k-2]):
                break
        xx=[]
    x1=[i for i in range(len(points))]
    x2=[i for i in range(len(val))]
    print "Minimum Value of the function is: ",evalf(x)
    print "Optimal solution is: ",x
    print "No. of iterations: ",k
    plt.scatter(x2,val,marker="*")
    plt.scatter(x1,points,marker=">")
    plt.title("Plot of f(x) in each iteration")
    plt.ylabel("f(x)")
    #plt.ylim(2.14826508530,2.14826508650)
    plt.show()

main()

