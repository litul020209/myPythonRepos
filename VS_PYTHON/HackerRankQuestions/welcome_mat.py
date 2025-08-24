m=int(input("enter the row : "))
n=int(input("enter the column: "))

c=".|."
d1=1
m1=m//2
for i in range (m1):
    print((c*(i+d1)).center(n,"-"))
    d1=d1+1
print("WELCOME".center(n,"-"))
d2=7
for i in range (m1):
    print((c*(d2-i)).center(n,"-"))
    d2=d2-1        
