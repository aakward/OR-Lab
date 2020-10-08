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
    #print nhbs
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
        

def kruskal():
    nbs=find_nhbs(tl,hd)   
    for i in range(len(hd)):
        for j in range(len(hd)-i-1):
            if wt[j]>wt[j+1]:
                temp=wt[j]
                wt[j]=wt[j+1]
                wt[j+1]=temp
                temp=hd[j]
                hd[j]=hd[j+1]
                hd[j+1]=temp
                temp=tl[j]
                tl[j]=tl[j+1]
                tl[j+1]=temp
    summ=0
    tl_n=[]
    hd_n=[]
    wt_n=[]
    c=0
    for i in range(len(wt)):
        #c=0 
        #while c==0:
            tl_n.append(tl[i]) 
            hd_n.append(hd[i]) 
            wt_n.append(wt[i])
            nhbs=find_nhbs(tl_n,hd_n)
            if (cycle(nhbs)==0):
#                mst.append(a)
#                mst.append(b)
                
                summ=summ+wt[i]
                print "The edge between nodes",tl[i],"and",hd[i],"with weight",wt[i],"is in the MST."
                c=c+1
                if(c==n-1):
                    break
            else:
                tl_n.pop()
                hd_n.pop()
                wt_n.pop()
                print "The edge between nodes",tl[i],"and",hd[i],"with weight",wt[i],"will not be in the MST or else there will be a cycle."
    print "The total edge weight in the MST is:",summ

    
        
kruskal()        
        
        
        
        
        
            
        
    