def product(m,n):
    if n==1:
        return m
    return m+product(m,n-1)


a=int(input("a: "))
b=int(input("b: "))
if b>a:
    a,b=b,a

print(product(a,b))