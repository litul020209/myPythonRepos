import random

a=True
while a==True:
    n=input("enter the choice you want  y/n: ").strip()
    v=n.lower()
    x=random.randint(1,6)
    y=random.randint(1,6)
    if v=="y" or v=="n":
        if v=="y":
            print(x,y)
        else:
            print("thanks for playing game")
            break
    else:
        # v!="y" or v != "n":
        print("please enter the valid decession")

    
    
        



