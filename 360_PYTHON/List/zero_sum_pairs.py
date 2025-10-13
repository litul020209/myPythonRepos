list1=[2, -2, 4, -4, 3]
ans=[]
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i]+list1[j]==0:
            ans.append((list1[i],list1[j]))

print(ans)