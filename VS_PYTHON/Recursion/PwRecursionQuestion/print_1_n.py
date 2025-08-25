
def print_1_to_n(n):
    if n==0:
        return 0
    
    print_1_to_n(n-1)
    print(n)


n=int(input("enter the n: "))
print(print_1_to_n(n))
i=1
while i<=n:
    print(i,end=" ")
    i=i+1

