


def oneD(arr):
    ans=[]
    for x in arr:
        for y in x:
            ans.append(y)
    return ans

arr=[[1,2,3],[4,5,6]]
print(oneD(arr))