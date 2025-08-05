
def find_last(arr,x):
    n=len(arr)
    if len(arr)==0:
       return -1
    if arr[n-1]==x:
        return 0
    ans=find_last(arr[0:n-1],x)
    if ans==-1:
        return -1
    else:
        return ans+1
   
x=int(input("enter the number: "))
arr=[3,2,5,2,8,2,1]
print(find_last(arr,x))
