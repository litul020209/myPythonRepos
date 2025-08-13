nums=[2,2,1,1,1,2,2]
# d={}
# for i in range(len(nums)):
#     count=1
#     for j in nums[i+1:]:
#         if j==nums[i]:
#             count+=1
#     if nums[i] not in d:
#         d[nums[i]]=count
#     else:
#         continue
# max_v=max(d.values())
# for k,v in d.items():
#     if v==max_v:
#         print(f"the most repeated digit in that list {k} with {v} repeation")

repeat=[]  
count=0  
for x in nums:
    if  x not in repeat:

        c=nums.count(x)
        if c>count:
            count=c
        repeat.append(x)
for y in nums:
    if nums.count(y)==count:
        print(y)
        break
