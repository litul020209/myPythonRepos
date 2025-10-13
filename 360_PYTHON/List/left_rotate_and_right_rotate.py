k=int(input(" enter the number of rotation: "))

nums=[10,20,30,40,50]

ans1=nums[k:]+nums[:k]

print(ans1)

ans2=nums[len(nums)-k:]+nums[:k+1]

print(ans2)