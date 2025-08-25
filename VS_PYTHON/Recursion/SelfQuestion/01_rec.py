def printNumber(l,u):
    if l>u:
        return
    printNumber(l+1,u)
    print(l)

print(printNumber(1,5))