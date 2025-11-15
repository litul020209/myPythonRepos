def isPrime(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True

def sum_prime_number(n,ans):
    if n!=0:
        if isPrime(n):
            print(n)
            ans=ans+n
        sum_prime_number(n-1,ans)
    else:
        print(ans)

num=int(input("num: "))
ans=0
sum_prime_number(num,ans)

