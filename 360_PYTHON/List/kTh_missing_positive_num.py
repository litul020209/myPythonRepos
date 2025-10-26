arr = [2,3,4,7,11]
k = 2

m=max(arr)
s1=set(range(1,m+1))
s_arr=set(arr)
ans=s1 - s_arr
ans=list(ans)
ans.sort()

print(ans[k-1])