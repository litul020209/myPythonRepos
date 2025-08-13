str1=["banana", "apple", "cherry", "date"]
n=len(str1)

for i in range(1,n):
    key=str1[i]
    j=i-1
    while j>=0 and str1[j]>key:
        str1[j+1]=str1[j]
        j=j-1
    str1[j+1]=key

print(str1)