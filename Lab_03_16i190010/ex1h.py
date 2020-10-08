import matplotlib.pyplot as plt
def evalf(x):
        value=x**2
        return value
def main():
        l=-10.0
        u=10.0
        r=0.9
        count=0
        while(abs(evalf(l)-evalf(u))>0.000001):
                count=count+1
                b=l+(r*(u-l))
                a=u-(r*(u-l))
                if(evalf(a)<evalf(b)):
                        u=b
                else:
                        l=a
        print evalf(l)
        print count
        value=[]
        points=[]
        for i in range (-15,16,1):
                points.append(i)
                value.append(evalf(i))
        plt.plot(points,value)
        plt.title("Plot of function f(x)=x^2 against x")
        plt.xlabel("x")
        plt.ylabel("x^2")
        plt.show()

main()

