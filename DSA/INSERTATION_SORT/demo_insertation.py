arr=[12,14,8,9,45,89,145,245,7,6,23]
n=len(arr)


for i in range(n):
    for j in range(i,-0,-1):
        if arr[j]<arr[j-1]:
            temp=arr[j-1]
            arr[j-1]=arr[j]
            arr[j]=temp
        else:
            break
print(arr)


