arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
arr3=[]

for n in arr2:
    for m in arr1:
        if n==m:
            arr3.append(m)
arr4=[]
for n in arr1:
    if n in  arr3:
        continue
    else:
        arr4.append(n)
arr4.sort()
ans=arr3+arr4
print(ans)





