x=int(input("enter the number x: "))
y=int(input("enter the number y: "))
z=int(input("enter the  number z: "))



def greater_number(x,y,z):
    if x>y:
        if x>z:
            print( x ," is bigger")
        else:
            print(z,"is bigger")

    elif y>x:
        if y>z:
         print(y,"is bigger")
        else:
            print(z,"is bigger")

greater_number(x,y,z)

