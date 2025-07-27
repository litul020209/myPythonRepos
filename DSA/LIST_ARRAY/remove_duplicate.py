nums = [1, 1, 1, 2, 2, 3, 4, 4, 5, 6, 7, 7, 8]
duplicate=0
p = 0
while p < len(nums) - 1:
    if nums[p] == nums[p + 1]:
        del nums[p]          # delete current if it's the same as next
        duplicate+=1    
          
    else:
        p += 1       # move to next only if current and next are different

count = len(nums)
print("Updated nums:", nums)
print("Unique count:", count)
for i in range(duplicate):
    nums.append("_")
print(nums)





       
