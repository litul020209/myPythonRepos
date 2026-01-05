def quick(arr,depth):
    if len(arr)<=1:
        return arr
    
    p=len(arr)-1
    less=[x for x in arr if x<arr[p]]
    equal=[x for x in arr if x==arr[p]]
    greater=[x for x in arr if x>arr[p]]

    sort_less=quick (less,depth+1)
    sort_great=quick(greater,depth+1)
    result=sort_less+equal+sort_great
    return result



arr=[2,8,4,9,3,7,1,5]
depth=0
print(quick(arr,depth))