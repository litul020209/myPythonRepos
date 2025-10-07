num1=int(input("num1:"))#16
num2=int(input("num2:"))#8
if num1>num2:
    num1,num2=num2,num1 
if num1<0:
    num1=-num1 
if num2<=0:
    num2=-num2
if  num1==0 or num2==0: 
    print(0) 
elif num1%num1==0 and num2%num1==0:
    print(num1)
else: 
    fact=num1
    while fact!=0: 
        if num1%fact==0 and num2%fact==0: 
            print(fact)
            break 
        fact-=1