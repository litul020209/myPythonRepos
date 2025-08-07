# def helper(str1):
#     pass

# def permutation(str1):   
#     pass

# str1="ab"
# print(permutation(str1))
from itertools import permutations
perm=permutations("abc")
ans=[]
for x in perm:
    y=list(x)
    str1=""
    for i in y:
        str1=str1+i
    ans.append(str1)

print(ans)    

