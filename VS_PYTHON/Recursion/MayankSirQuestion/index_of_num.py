def helper(arr,x,index):

    if len(arr)==0 or len(arr)==1:
        return index
    
    if arr[0]==x:
        return index
    index=index+1
    return helper(arr[1:],x,index)
    

def findFirstIndex(arr,x,index=0):
    return helper(arr,x,index)


arr=[3,6,2,1,7,2,2,3,9,2]
x=int(input("entert you want to find that index of a number: "))
print(findFirstIndex(arr,x))

