
def rabit_fibonacci(n):
    if n==0 or n==1:
        return 1
    ans=rabit_fibonacci(n-1)+rabit_fibonacci(n-2)
    return ans

num=12
print(rabit_fibonacci(num))
