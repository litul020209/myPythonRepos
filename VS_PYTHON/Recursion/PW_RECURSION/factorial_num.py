
def factorialNum(i,n,factorial):
    if i>n:
        return
    factorial=factorial*i
    print(f"{factorial} ", end=" ")
    factorialNum(i+1,n,factorial)


n=int(input("enter the number: "))
i=1
factorial=1
print(factorialNum(i,n,factorial))
print("\n")
while i<=n:
    factorial=factorial*i
    print(f"{factorial} ", end=" ")
    i=i+1

