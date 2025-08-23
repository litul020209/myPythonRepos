def printnum(n):
    if n==0:
        return 0
    printnum(n-1)
    print(n)
    return 
    

n=10
print(printnum(n))