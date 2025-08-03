list_01= [(1, 3), (2, 1), (3, 2)]
list_02=[]
for x in list_01:
    y=list(x)
    list_02.append(y)

a=True
while a==True:
    Swap=False
    n=len(list_02)-1
    for i in range(n):
        if list_02[i][1]>=list_02[i+1][1]:
            temp=list_02[i+1]
            list_02[i+1]=list_02[i]
            list_02[i]=temp
            Swap=True
    n=n-1
    if not Swap:
        break
list_03=[]
for x in list_02:
    y=tuple(x)
    list_03.append(y)
print(list_03)



    