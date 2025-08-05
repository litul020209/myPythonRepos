
def helper(arr1,arr2):
    if not arr1:
        return arr2
    minimum=min(arr1)
    arr1.remove(minimum)
    arr2.append(minimum)
    return helper(arr1,arr2)

def sortArrray(arr1,arr2):
    return helper(arr1,arr2)

arr1=[2,3,8,4,7,6,1,9,2,10,4,78]
arr2=[]
print(sortArrray(arr1,arr2))