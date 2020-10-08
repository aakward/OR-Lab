import math
import matplotlib.pyplot as plt

def evalf(x):
    y=1+math.pow(0.5,x)
    print y
    return y
def main():
    m=[]
    m.append(evalf(1))
    m.append(evalf(2))
    while(abs(m[len(m)-1]-m[len(m)-2])>0.000000001):
        m.append(evalf(len(m)+1))
    x_s=m[len(m)-1]
    print "The sequence converges to :",x_s

    h1=q_suplin(x_s,m)
    if(h1==1):
        print"Sequence is Superlinear"
    else:
        print "Sequence is not Superlinear"
    h2=q_lin(x_s,m)
    if(h2==1):
        print "Sequence is Q-Linear"
    else:
        print "Sequence is not Q-Linear"
    h3=q_quad(x_s,m)
    print "Sequence is Q-quadratically with M=",h3

    
def q_lin(x_s,m):
    x_star=[]
    x_star.append(x_s)
    flag=1
    f=int(len(m)/2)
    ratio=[]
    for i in range(f,len(m)):
        g1=[]
        g1.append(m[i])
        g2=[]
        g2.append(m[i-1])        
        d1=norm(g1,x_star)
        d2=norm(g2,x_star)
        ratio.append(d1/d2)
        if(d1>=d2):
            flag=0
    num=[i for i in range(len(ratio))]
    plt.scatter(num,ratio)
    plt.title("Plot eliciting convergence in Q-Linear")
    plt.ylabel("Ratios")
    plt.xlabel("Iterations")
    plt.show()
    plt.savefig("output3b_qlin")
    plt.clf()
    if(flag==1):
        return 1
    else:
        return 0
        
def q_suplin(x_s,m):
    if(m[len(m)-1]==x_s):
        return 1
    else:
        return 0

def q_quad(x_s,m):
    x_star=[]
    x_star.append(x_s)
    ratio=[]
    flag=1
    f=int(len(m)/2)
    for i in range(f,len(m)):
        g1=[]
        g1.append(m[i])
        g2=[]
        g2.append(m[i-1])        
        d1=norm(g1,x_star)
        d2=norm(g2,x_star)
        d2=d2**2
        ratio.append(d1/d2)
        maxm=max(ratio)
    num=[i for i in range(len(ratio))]
    plt.scatter(num,ratio)
    plt.title("Plot eliciting convergence in Q-Quadratic")
    plt.ylabel("Ratios")
    plt.xlabel("Iterations")
    plt.show()
    plt.savefig("output3b_qquad")

    return maxm
    
main()