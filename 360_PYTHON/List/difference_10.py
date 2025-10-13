nums=[5,8,25,27,40,42]
p=1
ans=[]
while p < len(nums):
    if nums[p]- nums[p-1] > 10:
        ans.append(nums[p])
    p+=1
print(ans)