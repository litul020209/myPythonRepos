import math

def lcm_01(num1,num2):
    m=num1*num2
    n=math.gcd(num1,num2)
    return m//n

def lcm_02(num1,num2):
    max_num=max(num1,num2)
    while True:
        if max_num%num1==0 and max_num%num2==0:
           return max_num
           break
    max_num=max_num+1


num1=8
num2=2
num_lcm1=lcm_01(num1,num2)
print(num_lcm1)
num_lcm2=lcm_02(num1,num2)
print(num_lcm2)

