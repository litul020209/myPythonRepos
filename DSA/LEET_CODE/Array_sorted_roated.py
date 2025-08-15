nums = [3,4,5,1,2]
m=nums.copy()
m.sort()
l=len(nums)-1

a=False
for i in range(l):
    if nums==m:
       a=True
       break
    w=nums[0]
    nums.remove(w)
    nums.append(w)
print(a)
