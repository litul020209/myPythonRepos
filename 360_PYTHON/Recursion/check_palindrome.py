def helper(num1,num2,num):
    if num1!=num2:
        return False
    return check(num)
        

def check(num):
    if len(str(num))==1:
        return True
    else:
        x=len(str(num))-1
        num1=num//10**x
        num2=num%10
        num=num-10**x
        num=num//10**(x-1)
        return  helper(num1,num2,num)
n=int(input("n: "))
print(check(n))