import numpy
from numpy.linalg import inv
import matplotlib.pyplot as plt
import math

def evalf(x):
        z=0
        for i in range(1,200):
                z=z+math.log(1+((i*x[i-1])-((i+1)*x[i])-i)**2)
        value=100-z
        print value
        return value

def gradf(x):
        z=0
        value=[]
        for i in range(1,200):
                z=0
                z=(float)(2*((i*x[i-1])-((i+1)*x[i])-i)*i)/(1+((i*x[i-1])-((i+1)*x[i])-i)**2)
                value.append(z)
        value.append((float)(-400*((199*x[198])-(200*x[199])-199))/(1+((199*x[198])-(200*x[199])-199)**2))
        return value

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
                lamb=lamb+5
                y=[]
                y1=[]
                for i in range(len(x)):
                    y.append(x[i]+lamb*d[i])
                    y1.append(x[i]+(lamb-1)*d[i])
        print "lamb=",lamb
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
                            l.append(a[i])
        print "Inner minima running"
        return l
        print "count= ",count



def main():
        y=[50 for i in range(200)]
        k=0
        x=[]
        m=[]
        m_grad=[]
        for i in range(len(y)):
            x.append(y[i])
        m.append(y)
        B=[]
        for i in range(200):
                temp=[]
                for j in range(200):
                        if(i==j):
                                temp.append(1)
                        else:
                                temp.append(0)
                B.append(temp)
        grad=gradf(x)
        m_grad.append(grad)
        grad2=[grad[i]**2 for i in range(len(grad))]
        while(math.sqrt(sum(grad2))>0.000001):
                B=numpy.linalg.inv(B)
                for i in range(200):
                        for j in range(200):
                                B[i][j]=-1*B[i][j]
                dir=numpy.matmul(B,grad)
                xx=inner_minima(x,dir)
                x=xx
                xx=[]
                print x
                m.append(x)
                grad=gradf(x)
                grad2=[grad[i]**2 for i in range(len(grad))]
                m_grad.append(grad)
                k=k+1
                s_k=[]
                y_k=[]
                for i in range(len(x)):
                        s_k.append(m[k][i]-m[k-1][i])
                        y_k.append(m_grad[k][i]-m[k-1][i])
                s1=0
                s2=0
                temp1=[]
                s_k_t=numpy.transpose(s_k)
                y_k_t=numpy.transpose(y_k)
                temp1=numpy.matmul(s_k_t,B)
                s1=numpy.matmul(temp1,s_k)
                s2=numpy.matpul(y_k_t,s_k)
                temp1=[]
                temp2=[]
                temp1=numpy.matmul(B,s_k)
                temp2=numpy.matmul(temp1,s_k_t)
                temp1=[]
                temp1=numpy.matmul(temp2,B)
                temp3=[]
                temp3=numpy.matmul(y_k,y_k_t)
                for i in range(len(temp1)):
                        for j in range(len(temp1)):
                                temp1[i][j]=(float)(-1*temp1[i][j])/s1
                                temp3[i][j]=(float)((temp3[i][j])/s2)
                B=B+temp1+temp3
        print "Optimal Solution is: ",x
        print "Minimum Value of the function is: ",evalf(x)
        print "No. of iterations: ",k

main()

