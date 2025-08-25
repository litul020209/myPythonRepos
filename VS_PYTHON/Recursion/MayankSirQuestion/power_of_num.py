def power(base,exp):
    if exp==1:
        return base
    ans=base*power(base,exp-1)
    return ans

base=int(input("enter the base num: "))
exp=int(input("enter the exponent : "))
print(power(base,exp))