num1=8
num2=16

while num2!=0:
    num3=num1
    num1=num2
    num2=num3%num2

print(num1)