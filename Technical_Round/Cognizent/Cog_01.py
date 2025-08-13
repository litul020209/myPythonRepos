arr1=[1,2,3,4,5]
arr2=[10,12,34,2,4,89]

max1=max(arr1)
min1=min(arr1)
max2=max(arr2)
min2=min(arr2)

r1=abs(max1-min2)
r2=abs(min1-max2)

if r1>r2:
    print(f" r1=={r1}")
else:
    print(f" r2=={r2}")
    