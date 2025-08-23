def  addsubset(ans,str1):
    list_01=ans.copy()
    
    for x in list_01:
        ans.append(str1[0]+x)
    return ans    

def subset(str1,ans):
    if not str1:
        return ans.append(" ")
    
    sans=subset(str1[1:],ans)
    
    if len(ans)==1:
        ans.append(str1[0])
   
    else:
        ans=addsubset(ans,str1)
      
    return ans

str1="abc"
ans=[]
result=subset(str1,ans)
result.remove(" ")
result.sort()
for x in result:
    print(x)
