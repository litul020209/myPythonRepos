
nums=[5,8,2,9,1]
min1=min(nums)
max1=max(nums)

for i in range(len(nums)):
    if nums[i]==min1:
        nums[i]=max1
    elif nums[i]==max1:
        nums[i]=min1

print(nums)
    
       