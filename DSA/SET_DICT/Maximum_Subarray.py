nums=[-2,1,-3,4,-1,2,1,-5,4]
res=[]
"""remove the all duplciates"""
sublists = [nums[i:j] for i in range(len(nums)) for j in range(i+1, len(nums)+1)]
print(len(sublists))

dict_sum={tuple(x):sum(x) for x in sublists }

max_list=[x for x in dict_sum.values()]
max_num=max(max_list)