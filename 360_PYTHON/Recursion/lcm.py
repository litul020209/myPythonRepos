def gcd(m,n):

    if m%n==0:
        return n
    temp=m
    m=n
    n=temp%m
    return gcd(m,n)

def lcm(m,n):
    return (m*n)// gcd(m,n)



a=int(input("a: "))
b=int(input("b: "))

if a>=b:
    print(lcm(a,b))
else:
    print(lcm(b,a))