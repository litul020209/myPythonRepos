def helper(arr,num,list_index,count):
    if not arr:
        return list_index
    if arr[0]==num:
        list_index.append(count)
    count=count+1
    return helper(arr[1:],num,list_index,count)


def list_indices(arr,num,list_index,count):
    return helper(arr,num,list_index,count)
    
arr=[3,2,5,2,8,2,1]
num=2
count=0
list_index=[]
print(list_indices(arr,num,list_index,count))
