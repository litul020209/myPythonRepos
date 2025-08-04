import array

def arrSum(arr):
    n=len(arr)
    if len(arr)==1:
        return arr[0]
   
    
    sans=arr[n-1]
    ans=sans+arrSum(arr[0:n-1])
    return ans
    

arr_01=array.array("i",[2,4,7,9,13,45,6])

print(arrSum(arr_01))