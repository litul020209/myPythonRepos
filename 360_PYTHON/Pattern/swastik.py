r=int(input("r: "))


for i in range(r):
    for j in range(r):
        if j==0 or j==(r-1):
            print("*",end=" ")
        elif i==(r-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    
    for j in range(r-1):
        if i==0 or i==(r-1):
            print("*",end=" ")
    print()

for i in range(r-1):
    for j in range(r):
        if j==(r-1) or i==(r-2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    for j in range(r):
        if j==(r-2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()