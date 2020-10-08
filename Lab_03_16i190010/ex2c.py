import matplotlib.pyplot as plt
def evalf(x1,x2,x3):
        value=0.0
        value=3*(x1**2)+0.05*(x2**4)+(10.0/(x3**2))
        return value
def main():
        l1=0
        l2=5
        l3=5
        u1=40.0
        u2=0
        u3=0.5
        value=[]
        points=[]
        for l in range(500):
                x1=l*l1+(1-l)*u1
                x2=l*l2+(1-l)*u2
                x3=l*l3+(1-l)*u3
                value.append(evalf(x1,x2,x3))
                points.append(l)
        plt.plot(points,value)
        plt.title("Plot of the function along the line joining (0,5,5) and (40,0,0.5)")
        plt.xlabel("lambda")
        plt.ylabel("Value of the function")
        plt.show()

main()
