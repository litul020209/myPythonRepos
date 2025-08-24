


def transpose(arr):
    a,b=arr[0],arr[1]
    ans=[]
    for x,y in zip(a,b):
        sans=[]
        sans.append(x)
        sans.append(y)
        ans.append(sans)
    return ans

mat = [
    [1, 2, 3],
    [4, 5, 6]
]
print(transpose(mat))