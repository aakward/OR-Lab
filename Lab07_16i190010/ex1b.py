import numpy  #for the following statement to compile successfully, you need the scikit-learn package. #You can install it using pip install -U scikit-learn or condai$
from sklearn.datasets import load_digits
digits = load_digits()
#check the shape of digits data
print(digits.data.shape)
#check the shape of digits target
print(digits.target.shape)
#let us use the linear regression used in the previous lab
N = digits.data.shape[0] #Number of data points
d1 = digits.data.shape[1] #Dimension of data points
Aa = digits.data
#In the following code, we create a Nx1 vector of target labels
ya = 1.0*numpy.ones([Aa.shape[0],1])
for i in range(digits.target.shape[0]):
        ya[i] = digits.target[i]
A=[]
for i in range(N):
        temp=[]
        for j in range(d1):
                temp.append(Aa[i][j])
        A.append(temp)
y=[]
for i in range(len(ya)):
        y.append(ya[i][0])

print type(A)
from numpy import linalg
from numpy.linalg import det
from numpy.linalg import inv
import math
At=numpy.transpose(Aa)
Ata=numpy.matmul(At,Aa)
ym=numpy.matrix(y)
ymt=numpy.transpose(ym)
Atb=numpy.matmul(At,ymt)

Kb=[]
x2=[0 for i in range(d1)]
start=[x2[i] for i in range(len(x2))]
def evalf(x):
        ye=numpy.matmul(A,x)
        err=[ye[i]-y[i] for i in range(len(y))]
        sum=0.0
        for i in range(len(y)):
                sum=sum+err[i]**2
        return 0.5*sum
def gradf(x):
        xm=numpy.transpose(numpy.matrix(x))
        z=numpy.matmul(Ata,xm)
#        zm=numpy.transpose(numpy.matrix(z))
#       print "zm=",zm
        grad=z-Atb
#       print "z1=",z1
        return grad
def alpha(y,d):
        alp=1000
        minimum=9999999999999
        min1=[999999]
        p=0
        while min1[p]<minimum:
                l=[]
                u=[]
                t=[]
                for i in range(len(y)):
                        l.append(y[i])
                        u.append(y[i]+alp*d[i])
                r=0.9
                kl=evalf(l)
                ku=evalf(u)
                while math.fabs(ku-kl)>10**(-12):
                        a=[]
                        b=[]
                        for j in range(len(l)):
                                b.append(l[j]+(r*(u[j]-l[j])))
                                a.append(u[j]-(r*(u[j]-l[j])))
                        ka=evalf(a)
                        kb=evalf(b)
                        if ka<kb:
                                u=[]
                                for j in range(len(b)):
                                        u.append(b[j])
                                ku=kb
                        else:
                                l=[]
                                for j in range(len(a)):
                                        l.append(a[j])
                                kl=ka
                c=min(kl,ku)
                if c==kl:
                        for i in range(len(l)):
                                t.append(l[i])
                else:
                        for i in range(len(u)):
                                t.append(u[i])

                min1.append(c)
                minimum=min1[p]
                p=p+1
                alp=alp+100
        return (t[1]-y[1])/d[1]
def distance(m,n):
        sum=0.0
        for i in range(len(m)):
                sum=sum+(m[i]-n[i])**2
        return math.sqrt(sum)



def bfgs(x):
        B=Ata
        k=0
        sum=0.0
        grad=gradf(x)
        Kb.append(0)
        for i in range(len(x)):
                sum=sum+math.fabs(grad[i])
        while sum>=10**(-5)*len(x):
                if det(B)==0:
                        print "determinant=0 break"
                        break
                k=k+1
                inverse=inv(B)
                grad=numpy.transpose(numpy.matrix(gradf(x)))
                d=numpy.matmul(inverse,grad)
                d=d.tolist()
                temp1=[]
                for i in range(len(d)):
                        for j in range(len(d[0])):
                                temp1.append(d[i][j])
                dir=[-temp1[i] for i in range(len(temp1))]
                temp=[x[i] for i in range(len(x))]
                alp=alpha(x,dir)
                for i in range(len(x)):
                        x[i]=x[i]+alp*dir[i]
                if x==temp:
                        print "Step Size=0 break"
                        break
                Kb.append(k)
                y=[gradf(x)[i]-gradf(temp)[i] for all in range(len(x))]
                s=[x[i]-temp[i] for i in range(len(x))]
                s1=numpy.transpose(numpy.matrix(s))
                st=numpy.matrix(s)
                y1=numpy.transpose(numpy.matrix(y))
                yt=numpy.matrix(y)
                p1=numpy.matmul(y1,yt)
                p1=p1.tolist()
                p2=numpy.matmul(yt,s1)
                p2=p2.tolist()
                p3=numpy.matmul(B,numpy.matmul(s1,numpy.matmul(st,B)))
                p3=p3.tolist()
                p4=numpy.matmul(st,numpy.matmul(B,s1))
                p4=p4.tolist()
                if p2[0][0]==0 or p4[0][0]==0:
                        print "denominator zero break"
                        break
                for i in range(len(B)):
                        for j in range(len(B[0])):
                                B[i][j]=B[i][j]+((-1)*p3[i][j]/p4[0][0])+(p1[i][j]/p2[0][0])
        return x

xstar=bfgs(start)
print "the optimal solution is ",xstar
print "the number of iterations are ",len(Kb)
print "the minimum value of the function is: ",evalf(xstar)
