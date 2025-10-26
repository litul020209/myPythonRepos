nums=[[12,23,44],[123,67],[12,66,78,7,9]]
ans=[]
for num in nums:
    for n in num:
        s=sum(num)
        ans.append(s)
print(max(ans))