from collections import deque

def Rotate(arr,k):
    if len(arr)==0 or k==0:
        return arr

    else:
        arr=deque(arr)
        arr.rotate(k)
        return arr


k=5
arr=[2,3,4,5,6,7]
print(Rotate(arr,k))