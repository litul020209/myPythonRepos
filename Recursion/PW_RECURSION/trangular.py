
def trangular(n):
    if n==1:
        return 1
    return n+trangular(n-1)

n=int(input("enter the n: "))
print(trangular(n))

