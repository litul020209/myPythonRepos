nums = [1,2,3,4,4]
# l=len(nums)
# a=False
# if l== 0 or l==1:
#     print(False)
# else:
#     for i in range(l-1):
#         for j in range(i+1,l):
#             if nums[i]==nums[j]:
#                 a=True
#                 break
            
# if a==True:
#     print(True)
# else:
#     print(False)
setans=set(nums)
if len(nums)==len(setans):
    print()   