nums1=[1,2,2,1]
nums2=[2,2]
l=len(nums2)
ans=[]
for i in range(len(nums1)-1):
    key=nums1[i]
    for j in range(l-1):
        if key==nums2[j]:
           ans.append(nums2[j])
           del nums2[j]
print(ans)
