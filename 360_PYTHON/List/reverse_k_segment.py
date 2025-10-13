nums=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
k=3
p=k
q=(p+k)-1
while q <=len(nums):
    if len(nums[p:]) >= 1:       
       nums[p:q+1]=nums[q:p-1:-1]
    p=p+6
    if len(nums[p:])<3:
           nums[p:]=nums[-1:p-1:-1]
           break
    q=(p+3)-1   
print(nums) 