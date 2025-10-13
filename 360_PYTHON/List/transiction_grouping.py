works= [100,200,300,400,500,600,700,800,900,1000]
ans=[]
list_7=[]
len=1
for num in works:
    list_7.append(num)
    if len==7:
        ans.append(list_7)
        list_7=[]
        len=0
    len+=1
ans.append(list_7)
print(ans)

