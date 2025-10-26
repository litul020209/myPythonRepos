
s1="abcddsaabcdefhijln"

set1=set(s1)

print(set1)

ans={x for x in set1   if s1.count(x) > 1}

print(ans)


