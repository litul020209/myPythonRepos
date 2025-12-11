from itertools import permutations as p
from itertools import combinations as c
from itertools import combinations_with_replacement as cr
try:
    l1=[10,20,30,40,50]

    print(list(p(l1,3)))
    print("-"*100)
    print(list(c(l1,3)))
    print("-"*100)
    print(list(cr(l1,3)))
except:
    print("check logic")