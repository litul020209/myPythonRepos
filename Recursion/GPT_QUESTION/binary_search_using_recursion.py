
def binarySearch(arr,target):    
    if not arr:
        return -1
    l=len(arr)
    start=0
    end=l-1
    mid=(start+(end-start))//2
    if len(arr)==1:
        if arr[mid]==target:
            ans=mid
            return ans
    elif arr[mid]==target:
        return mid
    else:
        if arr[mid]<target:
            ans= binarySearch(arr[mid+1:],target)
        else:
            ans= binarySearch(arr[0:mid+1],target)
    return ans
   
arr=[2,4,5,7,9,12,18,20,23,25]
target=25
print(binarySearch(arr,target))