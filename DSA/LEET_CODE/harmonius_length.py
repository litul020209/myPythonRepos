

nums = [1, 3, 2, 2, 5, 2, 3, 7]

ans=[]

for i in range(len(nums)):
    for j in range(i + 1, len(nums) + 1):
        temp=nums[i:j]
        print(temp)
        if len(ans)<=len(temp):
            m1=max(temp)
            m2=min(temp)
            if m1-m2==1:
                ans=temp


print(ans)