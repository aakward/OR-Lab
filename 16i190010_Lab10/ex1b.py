import net1 as G
m=[]
hd=G.hd
tl=G.tl
n2=G.n
wt=G.wt
w=dict()
for i in range(len(hd)):
    w[i]=wt[i]
s1=input("Enter the starting node : ")
t1=input('Enter the terminal node : ')


def nf(h,t):
    nodes=[]
    for i in h:
        if i not in nodes:
            nodes.append(i)
    for j in t:
        if j not in nodes:
            nodes.append(j)
    nodes.sort()
    return(nodes) 
    
def n_nodes(h,t):
    n=0    
    nodes=[]
    for i in h:
        if i not in nodes:
            nodes.append(i)
    for j in t:
        if j not in nodes:
            nodes.append(j)
    n=len(nodes)
    return(n)      

    
def find_nhbs(h,t):
    nbs=dict()
    nodes=nf(h,t)
    for no in nodes:
        nbs[no]=[]
    edges=[[h[i],t[i]] for i in range(len(h)) ]
    for e in edges:
        nbs[e[0]].append(e[1])
        nbs[e[1]].append(e[0])
    
    return(nbs)


def dfs(head,tail,s,t):
        n=n_nodes(head,tail)
        nbs=find_nhbs(hd,tl)
        nodes= nf(head,tail)
        edges_t=[(head[i],tail[i]) for i in range(len(head)) ]
        w3=dict()
        for e in edges_t:
            w3[e]=wt[edges_t.index(e)]
        for e in edges_t:
            w3[(e[1],e[0])]=w3[e]
        C=dict()
        ref_node=dict()
        for i in range(n):
            C[i+1]=sum(w.values())+1
            ref_node[i+1]="null"
        ref_node[s]=s    
        C[s]=0    
        flag2=0
        flag3=dict()
 
        stack=[s]
        not_visited=[s]
        it=0
        while not_visited!=[]:
            it=it+1
            l=len(stack)
            c=0
            for j in nbs[not_visited[-1]]:                   
                if C[j]>C[not_visited[-1]]+w3[(not_visited[-1],j)]:
                   C[j]=C[not_visited[-1]]+w3[(not_visited[-1],j)]
                   ref_node[j]=not_visited[-1]
                if j not in stack and c==0:
                    c=1
                    stack.append(j)
                    #break
            if len(stack)==l:
               not_visited.pop(len(not_visited)-1)
            else :
                not_visited.append(stack[-1])
                flag3[stack[-1]]=1                
        if ref_node[t]=="null":
            print "Nodes ",s,"and",t,"are not connected."
        else :
            print "Length of the shortest path from ",s,"to",t ,'is :',C[t]
            print "The number of iterations taken to compute the shortest path is :",it*(n-1)


dfs(hd,tl,s1,t1)

