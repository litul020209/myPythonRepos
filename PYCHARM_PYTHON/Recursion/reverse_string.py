
def helper(str1,ans):
    if len(str1)==1:
        ans=ans+str1
        return ans
    else:
        n=len(str1)-1
        ans=ans+str1[n]
        return helper(str1[:n],ans)


def reverse_string(str1):
    ans=""
    return helper(str1,ans)

str_0="lite Kumar"
print(reverse_string(str_0))