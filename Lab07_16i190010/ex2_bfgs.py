import numpy  #for the following statement to compile successfully, you need the scikit-learn package. #You can install it using pip install -U scikit-learn or condai$
import timeit
from numpy import linalg
from numpy.linalg import det
from numpy.linalg import inv
import math

def evalf(x):
#       print "x=",x
        yem=numpy.matmul(Aa,numpy.transpose(numpy.matrix(x)))
        yea=numpy.squeeze(numpy.array(yem))
#       print len(yea)
        ye=[yea[i] for i in range(len(yea))]
#       print "ye=",ye
        err=[ye[i]-y[i] for i in range(len(y))]
        sum=0.0
        for i in range(len(y)):
                sum=sum+err[i]**2
        sum1=0.0
        for i in range(d1):
                sum1=sum1+x[i]**2
        return 0.5*(sum+lamb*sum1)

def gradf(x):
      #  print "x",x
        lx=[lamb*x[i] for i in range(len(x))]
        #print "lx",lx
        lxm=numpy.transpose(numpy.matrix(lx))
       # print "lxm",lxm
        xm=numpy.transpose(numpy.matrix(x))
        #print "xm",xm        
        z=numpy.matmul(Ata,xm)
        #print "z",z
        grad=lxm+z-Atb
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
        return sum
def bfgs(x):
        B=hess
        k=0
        sum=0.0
        grad=numpy.squeeze(numpy.array(gradf(x)))
        Kb.append(0)
        for i in range(len(x)):
                sum=sum+math.fabs(grad[i])
        while sum>=10**(-5)*len(x):
                if det(B)==0:
                        print "determinant=0 break"
                        break
                k=k+1
                inverse=I
                d=numpy.matmul(inverse,gradf(x))
#               print "d=",d
                d=d.tolist()
#               print "d_new=",d
                temp1=[]
                for i in range(len(d)):
                        for j in range(len(d[0])):
                                temp1.append(d[i][j])
                dir=[-temp1[i] for i in range(len(temp1))]
#               print "direc=",dir
                temp=[x[i] for i in range(len(x))]
                alp=alpha(x,dir)
                
                for i in range(len(x)):
                        x[i]=x[i]+alp*dir[i]
                print evalf(x)
                if x==temp:
                        print "Step Size=0 break"
                        break
                Kb.append(k)
                gradx=numpy.squeeze(numpy.array(gradf(x)))
                gradt=numpy.squeeze(numpy.array(gradf(temp)))
                y=[gradx[i]-gradt[i] for all in range(len(x))]
#               print "y=",y
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
                p4=numpy.matmul(st,numpy.matmul(hess,s1))
                p4=p4.tolist()
                if p2[0][0]==0 or p4[0][0]==0:
                        print "denominator zero break"
                        break
                B=numpy.array(B)
#               print "B=",B
                for i in range(len(B)):
                        for j in range(len(B[0])):
                                B[i][j]=B[i][j]+((-1)*p3[i][j]/p4[0][0])+(p1[i][j]/p2[0][0])
        return x

N = 200
ds = [1000, 5000, 10000, 20000, 25000, 50000, 100000, 200000, 500000, 1000000]
lamb = 0.1
eps = numpy.random.rand(N,1) #random noise
time=[]
start_opt_diff=[]
opt_diff=[]
#For each value of dimension in the ds array, we will check the behavior of BFGS method
for i in range(numpy.size(ds)):
    d1=ds[i]
    print "Running for d=",d1
    Aa = numpy.random.randn(N,d1)
    xorig = numpy.ones((d1,1))
    ya = numpy.dot(Aa,xorig) + eps
    A=[]
    for i in range(N):
        temp=[]
        for j in range(d1):
                temp.append(Aa[i][j])
        A.append(temp)
    y=[]
    for i in range(len(ya)):
        y.append(ya[i][0])
    At=numpy.transpose(Aa)
    Ata=numpy.matmul(At,Aa)
    ym=numpy.matrix(y)
    ymt=numpy.transpose(ym)
    Atb=numpy.matmul(At,ymt)
    hess=lamb*numpy.identity(d1)+Ata
    I=inv(hess)
    Kb=[]
    x2=[1 for i in range(d1)]
    start=[x2[i] for i in range(len(x2))]
    time_start = timeit.default_timer()
    xstar=bfgs(start)
    bfgstime = timeit.default_timer() - time_start #time is in seconds
    
    print "time taken: ",bfgstime
    time.append(bfgstime)
    #print the total time and the L2 norm difference || x_opt - xorig|| for Newton method
    diff_start_opt=distance(xorig,xstar)
    print "The L2 norm difference between x_opt and x_orig is:",diff_start_opt
    start_opt_diff.append(diff_start_opt)
    v=numpy.dot(Aa,xstar)
    diff=distance(v,y)
    print "The L2 norm difference between A*x_opt and y is:",diff
    opt_diff.append(diff)
print "Time Summary: ",time
print "Distance between x_opt and x_orig Summary: ",start_opt_diff
print "Distance between A*x_opt and y Summary: ",opt_diff