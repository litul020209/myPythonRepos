num1=int(input())
num2=int(input())
num3=int(input())
#  if num1>num2 and num1>num3:
#     print("the num1 is bigger ")
# elif num2>num1 and num2>num3:
#     print("the num2 is bigger ")
# else:
#     print("the num3 is bigger ")  
if num1>num2:
    if num1>num3:
        print("the num1 is bigger ")     
    else:
        print("the num3 is bigger ")   
else:
   if num2>num3:
       print("the num2 is bigger  ")
   else:
       print("the num3 is bigger ")   