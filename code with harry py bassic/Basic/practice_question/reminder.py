
def reminder(num1,num2):
    if num1==0 or num2==0:
        return 0
    num3=num1//num2
    num4=num3*num2
    num5=num1-num4
    return num5

num1=int(input("enter the divident: "))
num2=int(input("enter the divider: "))

print(reminder(num1,num2))



    
    


