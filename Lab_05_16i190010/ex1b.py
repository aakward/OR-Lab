import math
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt

def evalf(x):
        value=((1-x[0])**2)+(100*((x[1]-x[0]**2)**2))
        return value

def gradf(x):
        dfdx1=-2*(1-x[0])-(400*x[0]*(x[1]-(x[0]**2)))
        dfdx2=200*(x[1]-(x[0]**2))
        grad=[]
        grad.append(dfdx1)
        grad.append(dfdx2)
        return grad

def hessf(x):
        hess=[]
        x1=x[0]
        x2=x[1]
        a=2+(1200*(x1**2))
        b=-400*x1
        c=200
        temp1=[]
        temp2=[]
        temp1.append(a)
        temp1.append(b)
        temp2.append(b)
        temp2.append(c)
        hess.append(temp1)
        hess.append(temp2)
        return hess
def inner_minima(x,d):
        y=[]
        y1=[]
        l=x
        u=[]
        r=0.9
        lamb=1
        for i in range(len(x)):
            y.append(x[i]+lamb*d[i])
            y1.append(x[i])
        while(evalf(y)<evalf(y1)):
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
        while(abs(evalf(l)-evalf(u))>10**(-15)):
                count=count+1
                b=[l[i]+(r*(u[i]-l[i])) for i in range(len(x))]
                a=[u[i]-(r*(u[i]-l[i])) for i in range(len(x))]
                if(evalf(a)<evalf(b)):
                        u=[]
                        for i in range(len(x)):
                            u.append(b[i])

                else:
                        l=[]
                        for i in range(len(x)):
                            l.append(a[i])
        return l
        print "count= ",count
def main():
                y=[-1,-1]
                k=0
                x=[]
                m=[]
                for i in range(len(y)):
                        x.append(y[i])
                m.append(y)
                H=hessf(x)
                H_inv=np.linalg.inv(H)
                grad=gradf(x)
                grad2=[grad[i]**2 for i in range(len(grad))]
                while(math.sqrt(sum(grad2))>0.0000001):
                        dir=[]
                        grad=gradf(x)
                        for i in range(len(grad)):
                                temp=0
                                for j in range(len(grad)):
                                        temp=temp+(H_inv[i][j]*grad[j])
                                dir.append(-1*temp)
                        grad2=[dir[i]**2 for i in range(len(dir))]
                        xx=inner_minima(x,dir)
                        x=xx
                        xx=[]
                        print x
                        m.append(x)
                        k=k+1
                        if(m[k]==m[k-1]):
                                break
                print "Optimal solution is: ",x
                print "Minimum Value of the function is: ",evalf(x)
                print "No. of iterations required is: ",k
                m1=[m[i][0] for i in range(len(m))]
                m2=[m[i][1] for i in range(len(m))]
                plt.scatter(m1,m2)
                plt.ylabel("Sequence of points")
                plt.title("Sequence of points generated by the algorithm")
                plt.xlabel("x[0]")
                plt.ylabel("x[1]")
                plt.show()
                dist=[]
                for i in range(1,len(m)):
                        d=0
                        d=((m[i][0]-m[i-1][0])**2)+((m[i][1]-m[i-1][1])**2)
                        dist.append(d)
                num=[i for i in range(len(dist))]
                plt.scatter(num,dist)
                plt.ylabel("Distances between consecutive points")
                plt.title("Plot of distances between consecutive points against no. of iterations")
                plt.xlabel("No. of iterations")
                plt.show()
                value=[]
                for i in range(len(m)):
                        value.append(evalf(m[i]))
                num2=[i for i in range(len(value))]
                plt.scatter(num2,value)
                plt.ylabel("function values")
                plt.xlabel("no. of iterations")
                plt.title("Plot of function values against no. of iterations")
                plt.show()


main()
