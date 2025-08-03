arr=[5,4,9,8,3,7,2,1]
a=True
while a==True:
    n=len(arr)-1
    p1=0
    p2=1
    swap=False
    for i in range(n):
        if arr[p1]>arr[p2]:
            temp=arr[p2]
            arr[p2]=arr[p1]
            arr[p1]=temp
            swap=True
        p1=p1+1
        p2=p2+1
    n=n-1
    if not swap:
        break

print(arr)
