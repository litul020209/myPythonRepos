l1=[1,2,3,4,5]
result=[]
for i in range(len(l1)):
    for j in range(i+1,len(l1)+1):
        result.append(l1[i:j])

print(result)