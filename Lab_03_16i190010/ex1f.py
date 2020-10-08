import matplotlib.pyplot as plt
def evalf(x):
        value=0.0
        value=(float)(0.0729*(x**6)-1.1664*(x**5)+7.7760*(x**4)-27.6480*(x**3)+55.2960*(x**2)-58.9284*x+26.2144)
        return value
def main():
        iter=[]
        size=[]
        for i in range (15,46,5):

                l=-i
                u=i
                r=0.9
                count=0
                size.append(u-l)
                while(abs(evalf(l)-evalf(u))>0.000001):
                        count=count+1
                        b=l+(r*(u-l))
                        a=u-(r*(u-l))
                        if(evalf(a)<evalf(b)):
                                u=b
                        else:
                                l=a
                print evalf(l)
                iter.append(count)
        plt.plot(size,iter,'ro')
        plt.title("Plot of no. of iterations against size of interval.")
        plt.xlabel("Size of interval")
        plt.ylabel("No. of iterations")
        plt.show()
main()



