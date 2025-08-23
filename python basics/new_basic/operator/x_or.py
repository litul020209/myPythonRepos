nums = [1, 2, 3, 6, 5, 4, 4, 2, 5, 3, 6, 1, 6, 5, 3, 2, 4, 1, 2, 5, 1, 4, 3, 6, 8, 4, 3, 1, 5, 6, 2] 
ans = 0
for x in nums:
    ans ^= x
print(ans)  # 3 (unique element)
# s=[10,11,12]
# n = 3
# for mask in range(1<<n):  # all 
#     subset = []
#     for i in range(n):
#         if mask & (1<<i):
#             subset.append(i)
#     print(subset)

# from itertools import combinations

# s ="ABC"
# # arr = list(s)  # make it indexable

# # all_subsets = []

# for r in range(len(s) + 1):  # r = size of subset
#     for combo in combinations(s, r):
#         l=list(combo)
#         a="".join(l)
#         print(a)
        # all_subsets.append(list(combo))

# for subset in all_subsets:
#     print(subset)
