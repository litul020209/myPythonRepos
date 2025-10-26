l1=[1,2,3,4,5,6]
res=[]
length=0
for i in l1:
    if i not in res:
        res+=[i]
        length+=1
    
result=[[]] 
result=result+[res[:]]

i1=-1
print(res)
for i in range(0,length):
    if [res[i]] not in result:
           result+=[[res[i]]]
    if res[i+1:] not in result:
            result+=[res[i+1:]]
    if res[:-i1] not in result:
          result+=[res[:-i1]]
    if res[i-1:-i1] not in result:
          result+=[res[i-1:-i1]]
    if res[-i1:i-1] not in result:
          result+=[res[-i1:i-1]]
    
    i1-=1
print(result)
print(len(result)-1)
