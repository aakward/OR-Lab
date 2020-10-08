param n;
param p;
set S :=1..n;
set P :=1..p;
param d{S};
param size{S};

var x{S,P}>=0,integer;
var t{P}>=0,integer;

minimize cost: sum{j in P} t[j];

s.t. con1 {i in S} : sum{j in P} x[i,j]*t[j] >= d[i];
s.t. con2 {j in P} : sum{i in S} x[i,j]*size[i] <=1030;
s.t. con3 {i in S,j in P} : x[i,j] <= 1030/size[i];
s.t. con4 {j in P} : 1030-(sum{i in S} size[i]*x[i,j])<=39;
s.t. con5 {j in P} : t[j]<=6603;