param N;  #total no. of patterns=496
param M;  #total no. of items
set S:=1..N;#patterns
set T:=1..M;#items
param PATTERNS{S,T};
param DEMAND{T};

var t{S}>=0, integer;


minimize cost: sum{j in S} t[j];

s.t. con1 {i in T}: sum{j in S} t[j]*PATTERNS[j,i]>=DEMAND[i];
