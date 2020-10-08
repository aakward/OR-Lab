import numpy as np

    
def rgraph(N,p):
    G=[]
    tpedges=N*(N-1)/2
    c=0
    G=[[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(i+1,N):
            r=np.random.binomial(1,p)
            G[i][j]=r
            G[j][i]=r
        
    print "The Edge Set of the graph is given as: "
    for i in range(len(G)):
        print G[i]


N=input("Enter the no. of vertices: ")
p=input("Enter p: ")
rgraph(N,p)