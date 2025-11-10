from math_operation.arithmetic.addition import add 
from math_operation.arithmetic.subtraction import subtract 
from math_operation.arithmetic.multiplication import multiply 
from math_operation.arithmetic.division import divide 
 

num1=int(input("num1: "))
num2=int(input("num2: "))
operation=input("enter the arithmatic operation: ")

match operation:
    case "+":
        res=add(num1,num2)
        print(f"{num1}+{num2} = {res}")
        
    case "-":
        res=subtract(num1,num2)
        print(f"{num1}-{num2} = {res}")
    case "*":
        res=multiply(num1,num2)
        print(f"{num1}*{num2} = {res}")
    case "/":
        res=divide(num1,num2)
        print(f"{num1}/{num2} = {res}")
    case _:
        print("Enter your correct operation")
      
       