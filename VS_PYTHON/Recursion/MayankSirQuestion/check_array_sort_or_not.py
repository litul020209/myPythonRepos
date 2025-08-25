def helper(arr1):
    if len(arr1)==1:
      return True
    
    elif arr1[0]>arr1[1]:
        return False
        
    return helper(arr1[1:])
    

def check_sort(arr1):
    return helper(arr1)

arr1=[1,2,3,4,5,1]
print(check_sort(arr1))
