from collections import Counter

def unique(count):
    ans=[]
    for k,v in count.items():
        if count[k]==1:
          ans.append(k)
    return ans

arr=[1,2,3,3,3,3,4,5]
count=Counter(arr)
print(unique(count))



