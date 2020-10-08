import math
import matplotlib.pyplot as plt

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
        y=[2.15 for i in range(1000)]
        k=0
        x=[]

        m=[]
        for i in range(len(y)):        
            x.append(y[i])
        
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
                    print xx
                    xx=[]
                    
                print x
                m.append(x)
                k=k+1
                if(m[k]==m[k-1]):
                        break
                
            
        print "Optimal solution is: ",x
        print "Minimum Value of the function is: ",evalf(x)
        print "No. of iterations: ",k

main()




