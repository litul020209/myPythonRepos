nums=[21,43,14,32,16,31,19,55,9]
nums1=[]
for n in nums:
    n=n%10
    nums1.append(n)
nums1.sort()
ans=[]

for m in nums1:
    for n in nums:
        r=n%10
        if m==r:
            if n not in ans:
               ans.append(n)

print(ans)


