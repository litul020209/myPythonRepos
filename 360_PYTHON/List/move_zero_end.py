nums=[0,1,2,0,3,4,0,5,6,7]
k=0
ans=[]
for i in range(len(nums)):
    if nums[i]==0:
        k+=1
    else:
        ans.append(nums[i])
print(ans)
print(k)

a=[0]*k
ans=ans+[0]*k
print(ans)