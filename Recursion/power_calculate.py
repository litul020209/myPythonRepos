def power(p,e):
    if e==0:
        return 1
    return p*power(p,e-1)
num=power(10,10)
print(num)