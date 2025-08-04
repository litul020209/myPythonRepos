letter=["a","b","c","d","e","f","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


n=int(input("enter the number: "))
m=n-1
d=1
for i in range(n-1):
    li=m
    k=0
    for j in range(i+d):
        if j<i+d//2:
           print(letter[li-j],end=" ")
        elif j>=i+d//2:
           print(letter[li+k],end=" ")
           k=k+1
           
    d=d+1
    print(" ")

