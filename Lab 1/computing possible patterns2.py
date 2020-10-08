
def main():
    x=[1000,980,940,920,900,710,700,650,640,630,60,55,50,45,40]
    count=0
    for a in range(2):
        for b in range(2):
            for c in range(2):
                for d in range(2):
                    for e in range(2):
                        for f in range(2):
                            for g in range(2):
                                for h in range(2):
                                    for i in range(2):
                                        for j in range(2):
                                            for k in range(18):
                                                for l in range(19):
                                                    for m in range(21):
                                                        for n in range(23):
                                                            for o in range(26):
                                                                value=((a*x[0])+(b*x[1])+(c*x[2])+(d*x[3])+(e*x[4])+(f*x[5])+(g*x[6])+(h*x[7])+(i*x[8])+(j*x[9])+k*x[10$
                                                                if(value<=1030):
                                                                    if(1030-value<40):
                                                                        count=count+1
                                                                        print(count)
    print("Total number of maximal patterns: ",count)

main()
