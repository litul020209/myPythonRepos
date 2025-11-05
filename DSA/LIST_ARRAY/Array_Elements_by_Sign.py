nums = [3,1,-2,-5,2,-4]
nums1=[x for x in nums if x > 0]
nums2=[x for x in nums if x < 0]

result=[list(x) for x in zip(nums1,nums2)]
