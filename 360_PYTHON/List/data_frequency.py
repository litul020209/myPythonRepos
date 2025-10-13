nums= [1,1,1,2,2,3,1,1,1,2,2,3,3,3,4]

new_num=list(set(nums))

ans=[]

for n in new_num:
    if n not in ans:
       ans.append((n, nums.count(n)))

print(ans)