import numpy as np
import random
import matplotlib.pyplot as plt

def rgraph2(N,K,p):
    G=[[0 for i in range(N)] for j in range(N)]
    
    K=K/2
    for i in range(N):
        k=1 
        for j in range(N):
            if (j>=i-K and j<=i+K and j!=i):
                G[i][j]=1
                if(i+K>N-1):
                    for l in range(i+K-N+1):
                        G[i][l]=1
                if(i-K<0):
                    for l in range(N-K+i,N):
                        G[i][l]=1
    sum1=0
    for i in range(len(G)):
        sum1=sum1+sum(G[i])
    print "No. of edges before the algorithm starts:",sum1/2
    
#    for i in range(len(G)):
#        print G[i]
        
    for i in range(N):
        for j in range(i+1,N):
            if G[i][j]==1:
                r=np.random.binomial(1,p)
                if(r==1):
                    G[i][j]=0
                    G[j][i]=0
                    flag=0
                    while(flag==0):
                        l=random.randint(0,N-1)
                        if(l!=i and G[i][l]==0):
                            G[i][l]=1
                            G[l][i]=1
                            flag=1
                        
    sum1=0
    for i in range(len(G)):
        sum1=sum1+sum(G[i])
    print "No. of edges after the algorithm finishes:",sum1/2

    
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
    
#    print "The Random Graph is: "
#    for i in range(len(G)):
#        print G[i]
            
    


N=input("Enter the no. of vertices: ")
p=input("Enter the value of p: ")
K=input("Enter a positive even no. 'K': ")
rgraph2(N,K,p)