import random
x=random.randint(1,100)
# while True:
#     strnum=input("enter your guessing number: ")
#     if strnum.isnumeric():
#         num=int(strnum)
#         if x==num:
#             print("Congratulation you guess the number. ")
#             break
#         elif num>x:
#             print("Too high!")
#         elif x>num:
#             print("Too low! ")

#     else:
#         print("enter the valid number! ")

while True:
    try:
       num=int(input("Enter your guessing number: "))
       if x==num:
             print("Congratulation you guess the number. ")
             break
       elif num>x:
            print("Too high!")
       else :
            print("Too low! ")
       
    except ValueError:
        print("enter the valid number ")