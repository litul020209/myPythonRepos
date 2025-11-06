def squareSum(num):
    if num==1:
        return 1
    return num**3+squareSum(num-1)



n=int(input("n: "))
print(squareSum(n))