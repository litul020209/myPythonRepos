nums=[30,36,38,32,40,41]
ans=[]
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        for k in range(j+1,len(nums)):
            if (nums[i]+nums[j]+nums[k] ) // 3 >35:
                ans.append([nums[i],nums[j],nums[k]])
           

print(ans)
