n=9

for i in range(n+1):
    for j in range(n,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print(j,end="")
        print(" ",end="")
    print()
for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    
    for j in range(1,n-i):
        print(j,end="")
        print(" ",end="")
    print()