nums1=[0,1,2]
nums2=[1,2,3]
ans_nums=[]

if ((len(nums1)==0 )or (len(nums1)==1))or ((len(nums2)==0) or (len(nums2)==1)):
   nums1.extend(nums2)
   for x in nums1:
      if x==0:
         continue
      else:
         ans_nums.append(x)

else:
    for x in nums1:
       ans_nums.append(x)
    for y in nums2:
       ans_nums.append(y)

ans_nums.sort()
print(ans_nums)

