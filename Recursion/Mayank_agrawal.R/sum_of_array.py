import array

def arrSum(arr):
    if len(arr)==1:
        return arr[0]
   
    
    sans=arrSum(arr[1:])
    ans=arr[0]+sans
    return ans
    

arr_01=array.array("i",[2,4,7,9,13,45,6])

print(arrSum(arr_01))