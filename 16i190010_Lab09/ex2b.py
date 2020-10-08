import net0 as G
tl=G.tl
hd=G.hd
n=G.n
wt=G.wt

def find_nhbs(tl_n,hd_n):
    nhbs=[[] for i in range(n)]
    for i in range(len(tl_n)):
        a=tl_n[i]-1
        b=hd_n[i]-1
        nhbs[a].append(b+1)
        nhbs[b].append(a+1)
    return nhbs
    
    
def cycle(nbs):
    #print nbs
    visited=[]  
    stack=[]
    stack.append(1)
    while(len(stack)!=0):
        a=stack.pop()
       # print "pop: ",a
        
        visited.append(a)
        for j in range(len(nbs[a-1])):
            if visited.count(nbs[a-1][j])==0:
                stack.append(nbs[a-1][j])
          #      print "push: ",nbs[a-1][j]
    cnt=[visited.count(i+1) for i in range(len(nbs))]
    flag=0
    for i in cnt:
        if i>1:
            flag=1
    if flag==1:
        return 1       #cycle present
    else:
        return 0
    
def prim():
    nbs=find_nhbs(tl,hd)
    edge_weights=[[1000000000 for j in range(n)] for i in range(n)]
    for i in range(len(tl)):
        a=tl[i]-1
        b=hd[i]-1
        edge_weights[a][b]=wt[i]
        edge_weights[b][a]=wt[i]
    tl_n=[]
    hd_n=[]
    wt_n=[]
    kk=0
    for i in range(n-1):
        edge_weights[i][i]=0
    mst=[]
    summ=0
    for i in range(n-1):
        c=0 
        while(c==0):
            minm=1000000
            a=-1
            b=-1
            for j in range(i+1):
                for k in range(n):
                    if edge_weights[j][k]<=minm and edge_weights[j][k]!=0:
                        minm=edge_weights[j][k]
                        a=j+1
                        b=k+1
            tl_n.append(a)
            hd_n.append(b) 
            wt_n.append(minm)
            nhbs=find_nhbs(tl_n,hd_n)
            if (cycle(nhbs)==0):
#                mst.append(a)
#                mst.append(b)
                
                summ=summ+edge_weights[a-1][b-1]
                print "The edge between nodes",a,"and",b,"with weight",edge_weights[a-1][b-1],"is in the MST."
                edge_weights[a-1][b-1]=0
                edge_weights[b-1][a-1]=0
                c=1
                kk=kk+1
            else:
                tl_n.pop()
                hd_n.pop()
                wt_n.pop()
                print "The edge between nodes",a,"and",b,"with weight",edge_weights[a-1][b-1],"will not be in the MST or else there will be a cycle."
                edge_weights[a-1][b-1]=9999
                edge_weights[b-1][a-1]=9999
    print "The total edge weight in the MST is:",summ
    print "Total no. of edges in the MST is: ",kk
    
                
prim()                
                
            
    
        
