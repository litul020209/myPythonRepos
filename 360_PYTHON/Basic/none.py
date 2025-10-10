# a=None
# print(a,type(a))
target=6
nums=[3,3]
p=0
for i in range(len(nums)-1):
    q=p+1
    while q <len(nums):
        if nums[p]+nums[q]==target:
            ans=[p,q]
            print(ans)
            break
        q+=1
    p+=1