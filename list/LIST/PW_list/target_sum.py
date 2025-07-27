nums=[2,7,11,15]
target=9
target_sum=[]
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==target:
            target_sum.append(i)
            target_sum.append(j)
            break

print(target_sum)
