from pulp import *
from input1b import *
N=len(w)
b=[]
objective=[]
for j in range(4280,4880,20):
    b.append(i)
for j in range(len(b)):     
    prob=LpProblem("problem1", LpMinimize)
    x=LpVariable.dicts("x", [i for i in range(N)], 0, 1, LpBinary)
    prob+= lpSum([c[i]*x[(i)] for i in range(N)])
    prob+= lpSum([w[i]*x[(i)] for i in range(N)])>=b[j]
    prob.solve()
    objective.append(value(prob.objective)
print(objective)