def search(arr,target):
    if not arr:
        return -1
    l=len(arr)
    start=0
    end=l-1
    mid=(start+(end-start))//2
    if arr[mid]==target:
        return mid
    else:
        if target>arr[mid]:
            ans=search(arr[mid+1:],target)
            if ans==0:
                ans=ans+1
           
            return ans+mid
        else:
            ans=search(arr[0:mid],target)
            return ans
              
arr=[2,4,7,9,12]
target=4

print(search(arr,target))


 