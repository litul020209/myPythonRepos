def isArmstrong(num,sum,x):
    if num!=0:
        digit=num%10
        sum=sum+(digit**length)
        num=num//10
        isArmstrong(num,sum,x)
    else:
        if sum==number:
            print("Armstrong Number")
        else:
            print("Not Armstrong number")

    
number=int(input("number: "))
sum=0
length=len(f"{number}")
isArmstrong(number,sum,length)