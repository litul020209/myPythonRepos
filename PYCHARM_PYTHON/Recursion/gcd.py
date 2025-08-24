
def gcd_euclid(a,b):
    if b==0:
        return a
    a,b=b,a%b
    return gcd_euclid(a,b)
num1=48
num2=18
print(gcd_euclid(num1,num2))