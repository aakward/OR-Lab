import numpy as np
import matplotlib.pyplot as plt
def main():
    mu1=2 #input("Enter the mean service time for the first set of customers: ")
    mu2=0.75 #input("Enter the mean service time for the second set of customers:")
    lmbda1=4 #input("Enter the mean inter-arrival time for the first set of customers: ")
    lmbda2=2 #input("Enter the mean inter-arrival time for the second set of customers: ")
    T=input("Enter the time horizon: ")
    WT1=[]
    WT2=[]
    UT=[]
    for b in range(1000):
        queue1=[]
        queue2=[]
        time=0
        while(time<=T):
            r=np.random.exponential(lmbda1)
            queue1.append(r)
            time=time+r
        time=0
        while(time<=T):
            r=np.random.exponential(lmbda2)
            queue2.append(r)
            time=time+r
        for i in range(1,len(queue1)):
            queue1[i]=queue1[i-1]+queue1[i]
        for i in range(1,len(queue2)):
            queue2[i]=queue2[i-1]+queue2[i]
        
        queue1.pop()
        queue2.pop()
        #print "Q1 ",queue1
        #print "Q2 ",queue2
        q1=queue1[:]
        q2=queue2[:]
        ser_end_times1=[]
        ser_end_times2=[]
        ser_end_time=[]
        if queue1[0]<=queue2[0]:
            r=np.random.exponential(mu1)
            ser_end_time.append(queue1[0]+r)
            ser_end_times1.append(queue1[0]+r)
            queue1.pop()
        else:
            r=np.random.exponential(mu2)
            ser_end_time.append(queue2[0]+r)
            ser_end_times2.append(queue2[0]+r)
            queue2.pop()
        while(len(queue1)>0 or len(queue2)>0):
            if(len(queue1)==0 and len(queue2)>0):
                r=np.random.exponential(mu2)
                ser_end_times2.append(max(ser_end_time[-1]+r,queue2[0]+r))
                ser_end_time.append(ser_end_times2[-1])
                queue2.pop()
            elif(len(queue2)==0 and len(queue1)>0):
                r=np.random.exponential(mu1)
                ser_end_times1.append(max(ser_end_time[-1]+r,queue1[0]+r))
                ser_end_time.append(ser_end_times1[-1])
                queue1.pop() 
            elif(queue1[0]<queue2[0]):
                r=np.random.exponential(mu1)
              #  ser_end_times1.append(queue1[0]+r)
                ser_end_times1.append(max(ser_end_time[-1]+r,queue1[0]+r))
                ser_end_time.append(ser_end_times1[-1])
                queue1.pop()
            else:
                r=np.random.exponential(mu1)
             #   ser_end_times1.append(queue1[0]+r)
                ser_end_times1.append(max(ser_end_time[-1]+r,queue1[0]+r))
                ser_end_time.append(ser_end_times1[-1])
                queue1.pop()
        #print "Service End Times for Q1",ser_end_times1
        #print "Service End Times for Q2",ser_end_times2
        wt1=[] 
        wt2=[]
        for i in range(len(ser_end_times1)):
            wt1.append(max(0,ser_end_times1[i]-q1[i]))
        for i in range(len(ser_end_times2)):
            wt2.append(max(0,ser_end_times2[i]-q2[i]))
        WT1.append(np.sum(wt1)/len(wt1))
        WT2.append(np.sum(wt2)/len(wt2))
        idle_times=0
        idle_times=min(q1[0],q2[0])
        Q=[]
        Q=q1+q2
        Q.sort()
        S_E_T=[]
        S_E_T=ser_end_times1+ser_end_times2
        S_E_T.sort()
        util=0
#        for i in range(len(Q)):
#            if(i!=len(Q)-1):
#                    idle_times=idle_times+max(0,Q[i+1]-S_E_T[i])
#        print idle_times,S_E_T[-1]
#        util=1.0-(idle_times/S_E_T[-1])
#        UT.append(util*100)
    print "Average Waiting Time for Queue 1 over 1000 simulations: ",np.sum(WT1)/len(WT1)
    print "Average Waiting Time for Queue 2 over 1000 simulations: ",np.sum(WT2)/len(WT2)
  #  print "Average Utilization of Server over 1000 simulations: ",np.sum(UT)/len(UT),"%"
    
    plt.hist(WT1)
    plt.title("Histogram of Waiting Times for Queue 1")
    plt.xlabel("Waiting Times")
    plt.ylabel("Frequency")
    plt.savefig("ex2a.png")
    plt.clf()
    plt.hist(WT2)
    plt.title("Histogram of Waiting Times for Queue 2")
    plt.xlabel("Waiting Times")
    plt.ylabel("Frequency")
    plt.savefig("ex2b.png")
    plt.clf()
    plt.plot(WT1,'ro')
    plt.title("Plot of Waiting Times of Queue 1 Across 1000 simulations")
    plt.xlabel("Simulations")
    plt.ylabel("Waiting Times")
    plt.savefig("ex2c.png")
    plt.clf()
    plt.plot(WT2,'ro')
    plt.title("Plot of Waiting Times of Queue 2 Across 1000 simulations")
    plt.xlabel("Simulations")
    plt.ylabel("Waiting Times")
    plt.savefig("ex2d.png")
    plt.clf()
#    plt.plot(UT,'ro')
#    plt.title("Plot of Utilization of Server Across 1000 simulations")
#    plt.xlabel("Simulations")
#    plt.ylabel("Utilization")
#    plt.savefig("ex2e.png")
#    plt.clf()
#    
    
            
    
main()