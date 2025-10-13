nums=[2,3,4,6,8,12]

target=24

ans=[]

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] * nums[j] ==target:
            if {nums[i],nums[j]} not in ans:
                ans.append({nums[i],nums[j]})
                break

for i in range(len(ans)):
    ans[i]=tuple(ans[i])

print(ans)





