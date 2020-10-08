import matplotlib.pyplot as plt
import numpy as np

    
def rgraph(N,p):
    G=[]
    tpedges=N*(N-1)/2
    c=0
    G=[[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        G[i][i]=0
    for i in range(N):
        for j in range(i+1,N):
            r=np.random.binomial(1,p)
            G[i][j]=r
            G[j][i]=r
    deg_distn=[]
    for i in range(len(G)):
        deg_distn.append(sum(G[i]))
    num=[]
    for i in range(0,N):
        num.append(i)
    freq=[]
    for i in range(len(deg_distn)):
        summ=0
        for j in range(len(deg_distn)):
            if deg_distn[j]==i:
                summ=summ+1
        freq.append(summ)
    plt.plot(num,freq)
    plt.xlabel("Degree")
    plt.ylabel("No. of nodes")
    plt.title("Plot of no. of nodes with degree 'd' against 'd'")
    
    
N=input("Enter the no. of vertices: ")
p=input("Enter p: ")
rgraph(N,p)