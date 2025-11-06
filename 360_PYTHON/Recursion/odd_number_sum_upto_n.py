def oddSum(n):
    
    if n==1:
        return 1
    ans=oddSum(n-1)+(n*2-1)
    return ans
    
    
n=int(input("n: "))
print(oddSum(n))