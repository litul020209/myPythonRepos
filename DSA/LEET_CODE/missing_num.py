nums = [0,1,0,3,12]
nums.sort()
l=len(nums)
print(f"so the total {l} digit in the list")
for i in range(l+1):
    if i in nums:
        continue
    else:
        print(i)
