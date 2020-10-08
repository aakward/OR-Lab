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
    return nhbs
    
def dfs():
    nbs=find_nhbs()
    #print nbs
    visited=[]  
    stack=[]
    stack.append(1)
    while(len(stack)!=0):
        a=stack.pop()
       # print "pop: ",a
        if visited.count(a)==0:
            visited.append(a)
        for j in range(len(nbs[a-1])):
            if visited.count(nbs[a-1][j])==0:
                stack.append(nbs[a-1][j])
          #      print "push: ",nbs[a-1][j]
    print "The sequence of nodes in the order they are visited are: ",visited
        

dfs()