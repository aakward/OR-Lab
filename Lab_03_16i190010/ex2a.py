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
        r=0.9
        count=0
        while(abs(evalf(l1,l2,l3)-evalf(u1,u2,u3))>0.000001):
                count=count+1
                b1=l1+(r*(u1-l1))
                a1=u1-(r*(u1-l1))
                b2=l2+(r*(u2-l2))
                a2=u2-(r*(u2-l2))
                b3=l3+(r*(u3-l3))
                a3=u3-(r*(u3-l3))
                if(evalf(a1,a2,a3)<evalf(b1,b2,b3)):
                        u1=b1
                else:
                        l1=a1
                if(evalf(a1,a2,a3)<evalf(b1,b2,b3)):
                        u2=b2
                else:
                        l2=a2
                if(evalf(a1,a2,a3)<evalf(b1,b2,b3)):
                        u3=b3
                else:
                        l3=a3
        print evalf(l1,l2,l3)
        print count

main()
