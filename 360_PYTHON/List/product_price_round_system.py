prices = [47.3, 53.9, 62.1, 78.4]
ans=[]
for num in prices:
    m=num//5
    n=m+1
    a1=m*5
    a2=n*5
    res1=num-a1
    res2=a2-num
    if res1<res2:
       ans.append(int(a1))
    else:
        ans.append(int(a2))
print(ans)
        
