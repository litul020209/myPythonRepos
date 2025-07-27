nums=[1,1,2,2,2,3,4,5,6,6,7,8,8,9]
value=2
i=0
count=0
while i<len(nums):
      if nums[i]==value:
            del nums[i]
            count+=1
      else:
            i+=1
print(f"total number of 2's in nums is {count}")
print(nums)
