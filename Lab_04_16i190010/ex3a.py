import math
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
        return l
        print "count= ",count

def main():
        y=[-1,-1]
        k=0
        x=[]

        m=[]
        x.append(y[0])
        x.append(y[1])
        m.append(y)
        e=[]
        for i in range(len(x)):
            temp=[]
            for j in range(len(x)):
                if i==j:
                        temp.append(1)
                else:
                        temp.append(0)
            e.append(temp)
        grad=gradf(x)
        grad2=[grad[i]**2 for i in range(len(grad))]
        while(math.sqrt(sum(grad2))>0.001):


                for i in range(len(x)):
                    d=e[i]
                    xx=inner_minima(x,d)
                    x=xx
                    xx=[]
                print x
                m.append(x)
                k=k+1
                if(m[k]==m[k-1]):
                        break
        print "Minimum Value of the function is: ",evalf(x)
        print "Optimal solution is: ",x
        print "No. of iterations: ",k

main()




