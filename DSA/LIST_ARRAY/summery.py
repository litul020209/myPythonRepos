nums=[]


p1=0
p2=1
k=nums[p1]
ans=[]
count=0
for i in range(len(nums)-1):
    
    if nums[p1]+1==nums[p2]:
        p1=p2
        p2+=1
        count+=1
    else:
        if count==0:
            ans.append([k])
        else:
            ans.append([k,nums[p1]])
        p1=p2
        p2+=1
        k=nums[p1]
        count=0
    if p1==len(nums)-1:
        ans.append([k,nums[p1]])                    
        break
result=[]
for x in ans:
    if len(x)==1:
        a=f"{x[0]}"
        result.append(a)
    elif x[0]==x[1]:
         a=f"{x[0]}"
         result.append(a)
    else:
        a=f"{x[0]}->{x[1]}"
        result.append(a)
print(result)

