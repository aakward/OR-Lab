from data2a import *
from pulp import *
a=[]
for i in range(n):
        temp=[]
        for j in range(n):
                if (i==j):
                        temp.append(1030/l[i])
                else:
                        temp.append(0)
        a.append(temp)
p=2
m=len(d)
while(p>1):
        prob1=LpProblem("Dual", LpMaximize)
        w=LpVariable.dicts("w", [i for i in range(n)],0,None,LpContinuous)
        prob1 += lpSum([d[i]*w[i] for i in range(n)])
        for j in range(m):
                prob1 += lpSum([w[i]*a[i][j] for i in range(n)])<=1
        prob1.solve()
        v=[]
        for i in prob1.variables():
                v.append(i.varValue)
        prob2=LpProblem("Knapsack", LpMaximize)
        y=LpVariable.dicts("y", [i for i in range(n)],0, None, LpInteger)
        prob2 += lpSum([v[i]*y[i] for i in range(n)])
        prob2 += lpSum([l[i]*y[i] for i in range(n)])<=1030
        prob2.solve()
        f=0
        for i in prob2.variables():
                a[f].append(i.varValue)
                f=f+1
        p=value(prob2.objective)
        print p
        c=0
        for i in range(len(d)):
                if a[i][m-1]==a[i][m-2]:
                        c=c+1
        if c==len(d):
                break
        m=m+1

prob3=LpProblem("Primal", LpMinimize)
t=LpVariable.dicts("t", [i for i in range(m)],0,None,LpContinuous)
prob3 += lpSum([t[i] for i in range(m)])
for i in range(n):
        prob3 += lpSum([a[i][j]*t[j] for j in range(m)])>=d[i]
prob3.solve()
print value(prob3.objective)
for i in prob3.variables():
        print "{}={}".format(i.name, i.varValue)

prob3 += lpSum([t[i] for i in range(m)])

