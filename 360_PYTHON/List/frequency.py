list1= ["error", "ok", "ok", "fail", "error"]
already=[]
ans=[]
for i in range(len(list1)):
    if list1[i] not in already:
        c=1
        for j in range(i+1,len(list1)):
            if list1[i]==list1[j]:
                c+=1
        ans.append((list1[i],c))
        already.append(list1[i]) 
       
print(ans)
              
