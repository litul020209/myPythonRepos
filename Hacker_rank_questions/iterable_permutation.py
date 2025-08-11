from itertools import permutations

s, n = input().split()   
n = int(n)
str1=s.upper()
ans=[]

# for length in range(1, len(S) + 1):
for p in permutations(str1,n):
    x="".join(p)
    ans.append(x)

print(ans)
ans.sort()
print(ans)
for word in ans:
    print(word)

# def permute(s, answer=""):
#     if len(s) == 0:
#         print(answer)
#         return
#     for i in range(len(s)):
#         ch = s[i]
#         left_substr = s[:i]
#         right_substr = s[i+1:]
#         rest = left_substr + right_substr
#         permute(rest, answer + ch)

# permute("ABC")
