
def naturalNumSum(n):
    if n==1:
        return 1
    sans=naturalNumSum(n-1)
    ans=n+sans
    return ans

res=naturalNumSum(10)
print(res)