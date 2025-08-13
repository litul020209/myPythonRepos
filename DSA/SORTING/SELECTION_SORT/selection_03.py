arr=[1,4,6,8,9,2,3,7,5]
n=len(arr)

for i in range(n-1):
    min_indx=i
    for j in range(i+1,n):
        if arr[j]<arr[min_indx]:
            min_indx=j
    temp=arr[min_indx]
    arr[min_indx]=arr[i]
    arr[i]=temp

print(arr)

    