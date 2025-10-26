nums = [3,4,5,2]

m1=max(nums)

print(m1)

if nums.count(m1) >1:
    m2=m1
else:
    second_list1=[]
    for x in nums:
        if m1!=x:
            second_list1.append(x)
    m2=max(second_list1)
print((m1-1)*(m2-1))