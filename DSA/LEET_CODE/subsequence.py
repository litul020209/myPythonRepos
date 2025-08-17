from itertools import combinations
s = "abc"
t = "ahbgdc"
result=[]
for combo in combinations(t, 3):
    result.append("".join(combo))

print(result)
if s in result:
    print(True)
else:
    print(False)