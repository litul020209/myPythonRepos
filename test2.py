from collections import Counter

nums = [1,2,2,3,1]

c = dict(Counter(nums))

v = [x for x in c.values()]

m=max(v)

if nums.count(m) == 1:
    
    