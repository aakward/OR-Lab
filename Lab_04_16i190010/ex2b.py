import math
import matplotlib.pyplot as plt
import numpy as np

val=[]
points=[]
iter=[]

def evalf(x):
    p=1
    v=0
    s2=[]
    s2=[x[i]**2 for i in range(len(x))]
    v=(sum(s2)/4000)
    for i in range(len(x)):
        p=p*math.cos(x[i]/((i+1)**0.5))
    v=v-p+1
    return(v)


def gradf(x):
    g=[0 for i in range(len(x))]
    for i in range(len(x)):
        p=1
        g[i]=2*x[i]/4000
        for j in range(len(x)):
            if i!=j:
                p=p*math.cos(x[j]/((j+1)**0.5))
        g[i]=g[i]+p*math.sin(x[i]/(i+1)**0.5)/((i+1)**0.5)
    return(g)

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
          #  l.append(x[i]-(lamb+1)*d[i])
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
                points.append(evalf(l))
                
        val.append(evalf(l))
        iter.append(count)
        return l
        print "count= ",count

    
def main():
        y=[-1 for i in range(10)]
        k=0
        x=[]

        m=[]
        for i in range(len(y)):        
            x.append(y[i])
        
        m.append(y)
        grad=gradf(x)
        grad2=[grad[i]**2 for i in range(len(grad))]
        while(math.sqrt(sum(grad2))>0.001):
                grad=gradf(x)
                d=[-grad[i] for i in range(len(x))]
                xx=inner_minima(x,d)
                x=xx
                xx=[]
                print x
                m.append(x)
                k=k+1
                if(m[k]==m[k-1]):
                        break
        x1=[i for i in range(len(points))]
        x2=[i for i in range(len(val))]
        print "Minimum Value of the function is: ",evalf(x)
        print "Optimal solution is: ",x
        print "No. of iterations: ",k
        plt.scatter(x2,val,marker="*")
        plt.scatter(x1,points,marker=">")
        plt.title("Plot of f(x) in each iteration")
        plt.ylabel("f(x)")
        plt.show()
        
main()
    