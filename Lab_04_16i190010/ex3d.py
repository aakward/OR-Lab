import math
import matplotlib.pyplot as plt

def evalf(p):
        v=(1+((p[0]+p[1]+1)**2)*(19-14*p[0]+13*p[0]**2-14*p[1]+6*p[0]*p[1]+3*p[1]**2))
        w=(30+((2*p[0]-3*p[1])**2)*(18-32*p[0]+12*p[0]**2-48*p[1]-36*p[1]*p[0]+27*p[1]**2))
        value=v*w
        return value
    
def gradf(p):
        grad=[]
        v=(2*(p[0]+p[1]+1)*(19-14*p[0]+13*p[0]**2-14*p[1]+6*p[0]*p[1]+3*p[1]**2)+((p[0]+p[1]+1)**2)*(-14+26*p[0]+6*p[1]))*(30+((2*p[0]-3*p[1])**2)*(18-32*p[0]+12*p[0]**2-48*p[1]-36*p[1]*p[0]+27*p[1]**2))
        u=(1+((p[0]+p[1]+1)**2)*(19-14*p[0]+13*p[0]**2-14*p[1]+6*p[0]*p[1]+3*p[1]**2))*(4*(2*p[0]-3*p[1])*(18-32*p[0]+12*p[0]**2-48*p[1]-36*p[1]*p[0]+27*p[1]**2)+((2*p[0]-3*p[1])**2)*(-32+24*p[0]-36*p[1]))
        grad.append(v+u)
        v1=(2*(p[0]+p[1]+1)*(19-14*p[0]+13*p[0]**2-14*p[1]+6*p[0]*p[1]+3*p[1]**2)+((p[0]+p[1]+1)**2)*(-14+6*p[0]+6*p[1]))*(30+((2*p[0]-3*p[1])**2)*(18-32*p[0]+12*p[0]**2-48*p[1]-36*p[1]*p[0]+27*p[1]**2))
        u1=(1+((p[0]+p[1]+1)**2)*(19-14*p[0]+13*p[0]**2-14*p[1]+6*p[0]*p[1]+3*p[1]**2))*(-6*(2*p[0]-3*p[1])*(18-32*p[0]+12*p[0]**2-48*p[1]-36*p[1]*p[0]+27*p[1]**2)+((2*p[0]-3*p[1])**2)*(-48-36*p[0]+54*p[1]))
        grad.append(v1+u1)
        return grad


def inner_minima(x,d):
        y=[]
        y1=[]
        l=[]
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
            l.append(x[i]-(lamb+1)*d[i])
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
        y=[0,0]
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
                if(m[k]==m[k-1] or len(m)==20):
                        break
        print "Minimum Value of the function is: ",evalf(x)
        print "Optimal solution is: ",x
        print "No. of iterations: ",k

main()




