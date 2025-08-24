def helper(str1,ans):
    if len(str1)==1:
        ans.append(str1)
        return ans
    helper(str1[1:],ans)
    a=str1[0]
    pans = ans[:]
    for x in pans:
        x=a+x
        ans.append(x)
    return ans

def subset(str1):

    ans=[]
    return helper(str1,ans)


str0="ABCD"
print(subset(str0))