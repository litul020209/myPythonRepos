a=int(input("enter the value of a : "))
b=int(input("enter the value of c : "))
c=int(input("enter the value of b : "))
x=a+b
y=b+c
z=c+a
if x>c:
    if y>a and z>c:
        print("the trangle creation is possible ")

    else:
        print("the tranle creation is not possible")

else:
    print("the tranle creation is not possible")   