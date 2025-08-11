def average(array):
    
    set_01=set(array)
    arr=list(set_01)
    s=sum(arr)
    t=len(arr)
    ans=s/t
    avg=round(ans,3)
    return avg
            
arr=[161,182,161,154, 176 ,170, 167, 171, 170, 174]
result = average(arr)
print(result)