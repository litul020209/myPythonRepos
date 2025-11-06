def gcd(m,n):

    if m%n==0:
        return n
    temp=m
    m=n
    n=temp%m
    return gcd(m,n)




a=int(input("a: "))
b=int(input("b: "))

if a>=b:
    print(gcd(a,b))
else:
    print(gcd(b,a))