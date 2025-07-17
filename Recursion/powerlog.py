def powerlog(base,exp):
    if exp==0:return 1
    if exp==1:return base
    if exp%2 ==0:
        total=powerlog(base,exp//2)
        ans=total*total
    else:
        total=powerlog(base,exp//2)
        ans=total*total*base
    
    return ans

res=powerlog(2,6)
print(res)