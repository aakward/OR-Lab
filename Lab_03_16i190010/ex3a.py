def evalf(x1,x2,x3):
        value=0.0
        value=3*(x1**2)+0.05*(x2**4)+(10.0/(x3**2))
        return value
def main():
        y1=7
        y2=2
        y3=0.1
        d1=-1
        d2=-0.2
        d3=0.5
        l1=7
        l2=2
        l3=0.1
        u1=40.0
        u2=0
        u3=0.5
        r=0.9
        lamb=1
        while(evalf(y1+lamb*d1,y2+lamb*d2,y3+lamb*d3)<evalf(y1,y2,y3)):
                lamb=lamb+1
        u1=y1+(lamb+1)*d1
        u2=y2+(lamb+1)*d2
        u3=y3+(lamb+1)*d3
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
                        u2=b2
                        u3=b3
                else:
                        l1=a1
                        l2=a2
                        l3=a3
        print "The optimal objective value is:",evalf(l1,l2,l3)
        print "The optimal solution is:",l1,l2,l3

main()
