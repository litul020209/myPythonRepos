nums=[1,4,6,8,9,2,3,7,5]
n=len(nums)

for i in range(n):
    mn=nums[i]
    indx=i
    for j in range(i+1,n):
        mn=min(mn,nums[j])
        indx=nums.index(mn)
    temp=nums[i]    
    nums[i]=mn
    nums[indx]=temp

print(nums)