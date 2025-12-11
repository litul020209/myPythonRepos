from collections import Counter

s1="aabbccddee"

print(dict(Counter(s1)))

l1=[4,2,3,5,7,9,1,4,3,7,8,4,5,0,3,2,1]
print(dict(Counter(l1)))

print((Counter(l1).most_common(1)))
print((Counter(l1).most_common(2)))