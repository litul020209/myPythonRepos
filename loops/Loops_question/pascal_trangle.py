num=[1,1]
n=int(input("enter the n th row: "))
for i in range(n+1):
    ans=[]
    for j in range(i+1):
        if j==0 or j==i:
            ans.append(1)            
            # print(1,end=" ")
        else:
            x=num[j-1]+num[j]
            ans.append(x)
            # print(x,end=" ")
 
    num=ans
    if i==n:
        print(ans)
    # print(" ")
 