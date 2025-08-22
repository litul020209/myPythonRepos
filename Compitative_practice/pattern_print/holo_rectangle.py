n=int(input("enter the m : "))
m=int(input("enter the n : "))

for i in range(n+2):
    for j in range(m+1):
        if i==0 or i==n+1:
            print("*",end="")
        elif i%2==0:
            
            if j==0 or j==m:
                print("*",end="")
            else:
                print(" ",end="")
        else:
            print(" ",end="")
    print("")
