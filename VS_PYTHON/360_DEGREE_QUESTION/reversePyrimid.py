n=5

for i in range(n):
    for j in range(i): #space in increase order 
        print(" ",end=" ")
    
    for j in range(i+1,n):
        print("*",end=" ")
    
    for j in range(i,n): #space in increase order 
        print("*",end=" ")



    print("\n")
    
