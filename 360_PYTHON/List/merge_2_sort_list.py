num1= [1,3,3,3,5,7]  
num2=[3,6,7,9]
p=0
q=0
ans=[]
while True:
    if num1[p] < num2[q]:
       if num1[p] not in ans:
          ans.append(num1[p])
       p+=1
    else:
        if num2[q] not in ans:          
           ans.append(num2[q])
        q+=1
    if p==len(num1)-1:
        ans=ans+num2[q:]
        break
    elif q==len(num2)-1:
        ans=ans+num1[p:]
        break
print(ans)

