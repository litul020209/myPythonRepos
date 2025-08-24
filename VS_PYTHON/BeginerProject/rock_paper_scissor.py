import random
import time

chars = ['R', 'P', 'S']

while True:
    user=input("rock,paper,scissor, R/P/S: ").upper()
    print("Spinning...")

    for i in range(10):
        pick = random.choice(chars)
        print(pick, end="\r")
        time.sleep(0.2)
    comp = random.choice(chars)

    if user in chars:
        if user=="R":
            if comp == "R":
                print("tie")
                ans=input("do you want to play more y/n: ").lower()
                if ans=="n":
                    break
            elif comp =="P":
                print("computer won")
                ans=input("do you want to play more y/n: ").lower()
                if ans=="n":
                    break

            else:
                print("You won")
                ans=input("do you want to play more y/n: ").lower()
                if ans=="n":
                    break
        elif user=="P":
            if comp == "P":
                print("tie")
                ans=input("do you want to play more y/n: ").lower()
                if ans=="n":
                    break
            elif comp =="S":
                print("computer won")
                ans=input("do you want to play more y/n: ").lower()
                if ans=="no":
                    break
            else:
                print("You won")
                ans=input("do you want to play more y/n: ").lower()
                if ans=="n":
                    break
        else:
            if comp == "S":
                print("tie")
                ans=input("do you want to play more y/n: ").lower()
                if ans=="n":
                    break
            elif comp =="R":
                print("computer won")
                ans=input("do you want to play more y/n: ").lower()
                if ans=="n":
                    break
            else:
                print("You won")
                ans=input("do you want to play more y/n only: ").lower()
                if ans=="n":
                    break
        
    else:
        print("enter the valid Decession ")
        
    
    

    
           




