import net0 as G
tl=G.tl
hd=G.hd
n=G.n
wt=G.wt

def find_nhbs():
    nhbs=[[] for i in range(n)]
    for i in range(len(tl)):
        a=tl[i]-1
        b=hd[i]-1
        nhbs[a].append(b+1)
        nhbs[b].append(a+1)
    print nhbs
    return nhbs
    
    
find_nhbs()