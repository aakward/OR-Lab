def main():
    patterns=[]
    x=[1000,980,940,640,630,60,55,50,45,40]
    count=0
    for a in range(2):
        for b in range(2):
            for c in range(2):
                for d in range(2):
                    for e in range(2):
                        for f in range(18):
                            for g in range(19):
                                for h in range(21):
                                    for i in range(23):
                                        for j in range(26):
                                            value=((a*x[0])+(b*x[1])+(c*x[2])+(d*x[3])+(e*x[4])+(f*x[5])+(g*x[6])+(h*x[7])+(i*x[8])+(j*x[9]))
                                            if(value<=1030):
                                                if(1030-value<40):
						    random=[]
						    random.append(a)
						    random.append(b)
						    random.append(c)
						    random.append(d)
						    random.append(e)
						    random.append(f)
						    random.append(g)
						    random.append(h)
						    random.append(i)
						    random.append(j)
						    patterns.append(random)							    	
                                                    count=count+1
                                                    print count



    print("The total number of maximal pattern is: ",count)
    print patterns
	




main()
