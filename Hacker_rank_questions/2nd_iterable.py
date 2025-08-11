from itertools import combinations

s, k = input().split()   
k = int(k)
str1 = ''.join(sorted(s.upper()))
print(str1)
# ans=[]

# for length in range(1, k+1):
#     for p in combinations(str1,length):
#         x="".join(p)
#         ans.append(x)


# result=[]
# for i in range(1,k+1):
#     small_result=[]
#     for x in ans:
#         if i==len(x):
            
#             small_result.append(x)
#     small_result.sort()
#     result.extend(small_result)
# print(result)
