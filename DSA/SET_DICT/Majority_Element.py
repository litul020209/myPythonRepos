nums = [3,2,3]
set_nums=set(nums)
dict_nums={x:nums.count(x) for x in set_nums}
m_list=[y for y in dict_nums.values()]
m=max(m_list)
for k in dict_nums.keys():
    if dict_nums[k]==m:
        print(k)
        break