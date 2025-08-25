def pattern(n):
    if n==0:
        return 
    pattern(n-1)
    print("*"*n)
    
n=int(input("enter the number: "))
print(pattern(n))