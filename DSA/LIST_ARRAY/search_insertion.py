nums = [1,3,5,6] #this list is sorted
target = 4
i=0
while i<len(nums):
    if nums[i]>=target:
        print(i)
        break

    i=i+1
else:
        print(len(nums))
    


    
    