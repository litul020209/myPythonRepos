def squareSum(num):
    if num==1:
        return 1
    return num**2+squareSum(num-1)



n=int(input("n: "))
print(squareSum(n))