n=5
m=6

for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print("\n")
for i in range(m):
    for j in range(i):
        print(" ",end=" ")
    
    for j in range(i,m):
        print("*",end=" ")
    
    for j in range(i+1,m):
        print("*",end=" ")
    print("\n")

