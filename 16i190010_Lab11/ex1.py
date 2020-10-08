import matplotlib.pyplot as plt
import numpy as np
def main():
    mu1=2 #input("Enter the mean service time for the first set of customers: ")
    mu2=0.75 #input("Enter the mean service time for the second set of customers:")
    lmbda1=4 #input("Enter the mean inter-arrival time for the first set of customers: ")
    lmbda2=2 #input("Enter the mean inter-arrival time for the second set of customers: ")
    T=input("Enter the time horizon: ")
    
    WT=[]
    UT=[]
    for b in range(1000):    ##
        queue=[]
        time=0
        c_q1=0
        c_q2=0
        Idle_times=[]
        while time<=T:
            if(c_q1<=time):
                r1=np.random.exponential(lmbda1)
                #print "Inter Arrival Type 1",r1
                c_q1=c_q1+r1
                queue.append([r1+time,1])
            if(c_q2<=time):
                r2=np.random.exponential(lmbda2)
                #print "Inter Arrival Type 2",r2    
                c_q2=c_q2+r2
                queue.append([r2+time,2])
            time=time+min(r1,r2)
        
        queue.sort()
        #print queue
        #print "Arrival times: "
#        for i in range(len(queue)):
#            print queue[i][0]
        
        service_end_times=[]
        if(queue[0][1]==1):
                r=np.random.exponential(mu1)
        else:
                r=np.random.exponential(mu2)
        s=queue[0][0]+r
        service_end_times.append(s)
        for i in range(1,len(queue)):
            if(queue[i][1]==1):
                r=np.random.exponential(mu1)
            else:
                r=np.random.exponential(mu2)
            s=max(service_end_times[i-1]+r,queue[i][0]+r)
            service_end_times.append(s)
        #print "Service End Times: ",service_end_times
        waiting_times=[]
        idle_time=queue[0][0]
        for i in range(len(queue)):
            waiting_times.append(service_end_times[i]-queue[i][0])
            if(i!=len(queue)-1):
                idle_time=idle_time+max(0,queue[i+1][0]-service_end_times[i])
        #print "WT", waiting_times
        #Idle_times.append(idle_time)
    
        WT.append(np.sum(waiting_times)/len(queue))
        util=1.0-(idle_time/service_end_times[-1]) 
        UT.append(util*100) 
    #print "Server Utilization: ",util*100,"%"
    
    print "Average waiting time over 1000 simulations: ",np.sum(WT)/len(WT)
    print "Average Utilization of server over 1000 simulations: ",np.sum(UT)/len(UT),"%"
    num=[i for i in range(1,1001)]    
    plt.plot(WT,'ro')
    plt.title("Plot of Waiting Times Across 1000 simulations")
    plt.xlabel("Simulations")
    plt.ylabel("Waiting Times")
    plt.savefig("ex1a.png")
    plt.clf()
    plt.plot(UT,'ro')
    plt.title("Plot of Utilization of Servers Across 1000 simulations")
    plt.xlabel("Simulations")
    plt.ylabel("Utilization")
    plt.savefig("ex1b.png")
    plt.clf()
    
    
    
main()
        
        
        
    