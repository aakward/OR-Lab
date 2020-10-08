from pulp import *
from input1 import *
N=len(w)
prob=LpProblem("problem1", LpMinimize)
x=LpVariable.dicts("x", [i for i in range(N)], 0, 1, LpBinary)
prob+= lpSum([c[i]*x[(i)] for i in range(N)])
prob+= lpSum([w[i]*x[(i)] for i in range(N)])>=b
prob.solve()
print LpStatus[prob.status]
print value(prob.objective)
for v in prob.variables():
        print "{}={}".format(v.name, v.varValue)