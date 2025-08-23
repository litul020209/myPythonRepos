
def helper(str1,rstr):
    n=len(str1)
    if len(str1)==0:
        return rstr
    strn=str1[n-1]
    rstr=rstr+strn
    return helper(str1[:n-1],rstr)


def reverse(str1,rstr):
    return helper(str1,rstr)

str1="abcd"
rstr=""
print(reverse(str1,rstr))

