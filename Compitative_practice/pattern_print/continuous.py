n=int(input("enter the number: "))
sum=0
for i in range(n):
    
    for j in range(i+1):
        sum+=1
        print(sum,end=" ")
    print("")
        