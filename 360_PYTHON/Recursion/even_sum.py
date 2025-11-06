def evenSum(n):
    
    if n==1:
        return 2
    ans=evenSum(n-1)+(n*2)
    return ans
    
    
n=int(input("n: "))
print(evenSum(n))