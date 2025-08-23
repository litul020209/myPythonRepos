def binary_convert(number):
    x=number
    
    str_n1=""
    while x>= 1:
        b=x%2
        str_n1=str(b)+str_n1
        x=x//2
    
    return str_n1


def count_1(a):
    count_1=0
    for i in a:
        if i==str(1):
            count_1=count_1+1
        else:
            pass
    return count_1

number=int(input("enter the number : "))
n1=binary_convert(number)
n2=count_1(n1)
print("the 1 present in this binary number is : ", n2)