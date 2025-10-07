
n=int(input("Enter the Number: "))

for i in range(n):
    for j in range(1,i+2):
        if j%2==0:
            print(0,end=" ")
        else:
            print(1,end=" ")
    
    for j in range(n-1,i,-1):
        print(" ",end=" ")

    for j in range(n-2,i,-1):
        print(" ",end=" ")

    for j in range(1,i+2):
        if j%2==0:
            print(0,end=" ")
        else:
            if i==(n-1):
                if j==1:
                    continue
            print(1,end=" ")
    print()
    
for i in range(n-1):
    for j in range(n-1,i,-1):
        if j%2==0:
            print(1,end=" ")
        else:
            print(0,end=" ")
    
    for j in range(i+1):
        print(" ",end=" ")
    
    for j in range(i):
        print(" ",end=" ")

    for j in range(n-1,i,-1):
        if j%2==0:
            print(1,end=" ")
        else:
            print(0,end=" ")
    print()