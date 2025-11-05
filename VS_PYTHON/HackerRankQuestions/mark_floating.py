n=int(input("n: "))

while n!=0:
    n-=1
    x=input("x: ")
    if "." in x:
        y=x.split(".")
        if y[0][0]=="+" or y[0][0]=="-":
            if y[0][1:].isnumeric() and y[1].isnumeric():
                print(True)
            else:
                print(False)
        else:
            print(False)
    else:
        print(False)