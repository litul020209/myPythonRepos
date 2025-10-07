n=int(input("enter the number: "))

for i in range(n):
    for j in range(1,i+2):
        print(j,end=" ")
    for j in range(i,n-1):
        print("*",end=" ")
    
    for j in range(i,n-1):
        print("*",end=" ")
    d=i+1
    for j in range(1,i+2):
        print(d,end=" ")
        d=d-1
    print()
        
    
    

