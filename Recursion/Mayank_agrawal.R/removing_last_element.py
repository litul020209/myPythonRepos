def helper(arr,num):
    n=len(arr)
    if len(arr)==0:
       return 
    num=arr[n-1]
    print (num)
    return helper(arr[:n-1],num) 

def removelast(arr,last_num):
    return helper(arr,last_num)
    
arr=[1,2,3,4,5,6]
last_num=0
print(removelast(arr,last_num))