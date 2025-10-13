nums= [2, 4, 3, 6, 12, 10]
ans=[]
for i in range(len(nums)):
    if i==0:
        continue
    else:
        if nums[i]== 2*nums[i-1]:
            ans.append(i)
print(ans)        

