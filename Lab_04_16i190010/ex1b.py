import math
import matplotlib.pyplot as plt
def evalf(x1,x2):
        value=((1-x1)**2)+(100*((x2-x1**2)**2))
        return value

def gradf(x1,x2):
        dfdx1=-2*(1-x1)-(400*x1*(x2-(x1**2)))
        dfdx2=200*(x2-(x1**2))
        grad=[]
        grad.append(dfdx1)
        grad.append(dfdx2)
        return grad

def inner_minima(x,d):
        y=x
        l=x
        r=0.9
        lamb=1
        while(evalf(y[0]+lamb*d[0],y[1]+lamb*d[1])<evalf(y[0]+(lamb-1)*d[0],y[1]+(lamb-1)*d[1])):
                lamb=lamb+1
        u1=y[0]+(lamb+1)*d[0]
        u2=y[1]+(lamb+1)*d[1]
        count=0
        while(abs(evalf(l[0],l[1])-evalf(u1,u2))>10**(-12)):
                count=count+1
                b1=l[0]+(r*(u1-l[0]))
                a1=u1-(r*(u1-l[0]))
                b2=l[1]+(r*(u2-l[1]))
                a2=u2-(r*(u2-l[1]))
                if(evalf(a1,a2)<evalf(b1,b2)):
                        u1=b1
                        u2=b2
                else:
                        l[0]=a1
                        l[1]=a2
        l1=[]
        l1.append(l[0])
        l1.append(l[1])
        return l1        
        print "count= ",count
        
def main():
        y=[-1,-1]
        k=0
        x=[]
        x1=-1
        x2=-1
        m=[]
        x.append(x1)
        x.append(x2)
        m.append(y)
        grad=gradf(x1,x2)
        while(math.sqrt((grad[0]**2)+(grad[1]**2))>0.001):
                d=[]
                grad=gradf(x[0],x[1])
                d1=-grad[0]
                d2=-grad[1]
                d.append(d1)
                d.append(d2)
                xx=inner_minima(x,d)
                x1=xx[0]
                x2=xx[1]
                k=k+1
                print xx
                m.append(xx)
                xx=[]
        print "Minimum Value of the function is: ",evalf(x1,x2)
        print "Optimal solution is: ",x
        print "No. of iterations: ",k
        mx=[]
        my=[]        
        for i in range(len(m)):
            mx.append(m[i][0])
            my.append(m[i][1])
        plt.scatter(mx,my)
        plt.xlabel("x1")
        plt.ylabel("x2")
        plt.title("Plot of sequence of points")
        plt.savefig("ex1f")


main()
