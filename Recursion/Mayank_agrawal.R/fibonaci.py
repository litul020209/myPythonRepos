def fibonacii(n):
    if n==0:
        return 1
    if n==1:
        return 1
    secndPrev=fibonacii(n-2)
    prev=fibonacii(n-1)
    
    ans=prev+secndPrev
    return ans

n=int(input("enter the number:  "))
print(fibonacii(n))