nums=[1,2,3,4,5]
ans=[0]*len(nums)
for i in range(1,len(nums)-1):
    ans[i]=nums[i]+nums[i-1]

ans[0]=nums[0]
ans[len(ans)-1]=nums[len(nums)-1]

print(ans)