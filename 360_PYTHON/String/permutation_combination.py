from itertools import permutations as p
from itertools import combinations as c

s="ABC"
ans1=[]
for r in range(len(s)+1):
    for x in p(s,r):
        a1="".join(x)
        print(a1)
ans2=[]
for r in range(len(s)+1):
    for x in c(s,r):
        a2="".join(x)
        print(a2)
