list1=["a","a","b","c","a","a","a","d","d"]

p=0
q=1

ans=[]
while q< len(list1):
    if list1[p]==list1[q]:
        q+=1
    else:
        ans.append(list1[p])
        p=q
        q=q+1

ans.append(list1[p])
print(ans)