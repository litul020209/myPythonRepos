


def unique_element(arr1):
    d={}
    for x in arr:
        d[x]=d.get(x,0)+1
    res=list(filter(lambda y: d[y]==1 ,arr1))
    return res



arr=[1,2,3,4,6,1,2,3,3,4,6,7,8,8,9,1,2,3,5]
print(unique_element(arr))