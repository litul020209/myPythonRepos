def helper(num1,num2,x):
    if num1%10==num1:
        return num1+num2
    small_num=num1%10
    num2=num2+small_num*10**x
    num1=num1//10
    return helper(num1,num2,x-1)


def reverseNum(num1,num2):
    x=len(str(num1))-1
    return helper(num1,num2,x)


n=int(input("n: "))
new_num=0
print(reverseNum(n,new_num))