nums1 = [-1,0,0,3,3,3,0,0,0]
nums2 = [1,2,2]

m=5
n=2
k=8

while n>=0:
      if m<0 or nums2[n]>nums1[m]:
            nums1[k]=nums2[n]
            n=n-1
            k=k-1
      else:
            
            m=m-1
nums1.sort()
print(nums1)





# nums3=[]
# for i in range(len(nums1)-1):
#     if nums1[0]<=0:
#         nums3.append(nums1[0])
#         nums1.remove(nums1[0])
#     else:
#         break


# nums1.extend(nums2)
# nums1.sort()
# for i in range (len(nums1)-1):
#     if nums1[0]==0:
#         nums1.remove(0)
#     else:
#         break
# nums3,nums1=nums1,nums3
# nums1.extend(nums3)
# print(nums1)