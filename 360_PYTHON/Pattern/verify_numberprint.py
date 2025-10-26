n=int(input("Enter the row: "))
s=(n-1)*2 
for i in range(1,n+1):
    
    for j in range(s):
       print(" ",end=" ")
    d=i
    m=i*2-1
    e=m-1
    for j in range(i*2-1):
        if d<=m:
          print(d,end=" ")
          d=d+1
        else:
           print(e,end=" ")
           e=e-1
    s=s-2
    print()
    
       
            
   






