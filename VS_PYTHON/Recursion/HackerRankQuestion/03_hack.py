def fibonacci(n):
    if n==0 or n==1:
        return n
    ans=fibonacci(n-1)+fibonacci(n-2)
    return ans

n=int(input("enter the num: "))
print(fibonacci(n))