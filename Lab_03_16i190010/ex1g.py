import matplotlib.pyplot as plt
def evalf(x):
        value=0.0
        value=(float)(0.0729*(x**6)-1.1664*(x**5)+7.7760*(x**4)-27.6480*(x**3)+55.2960*(x**2)-58.9284*x+26.2144)
        return value
def main():
        r=[0.99,0.95,0.9,0.8,0.7,0.6,0.55,0.4,0.3,0.2,0.1,0.001]
        iter=[]
        for i in r:
                count=0
                l=-10.0
                u=10.0
                while(abs(evalf(l)-evalf(u))>0.000001):
                        count=count+1
                        b=l+(i*(u-l))
                        a=u-(i*(u-l))
                        if(evalf(a)<evalf(b)):
                                u=b
                        else:
                                l=a
                iter.append(count)
                print count
        plt.plot(r,iter,'ro')
        plt.title("Plot of No. of iterations against r")
        plt.xlabel("value of r")
        plt.ylabel("No. of iterations")
        plt.show()
main()

