nums=[1,1,2,2,3,1,2,2,1,1,1,1,1,1,1,1,2]
ans=[]
p=0
while p < len (nums)-1:
      if nums[p+1]==nums[p]:
            p+=1
      else:
          ans.append(nums[p])
          p+=1
ans.append(nums[len(nums)-1])
print(ans)