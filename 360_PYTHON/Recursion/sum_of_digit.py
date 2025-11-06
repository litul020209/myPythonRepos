def sumOfDigit(num):
    if num%10==num:
        return num
    return (num%10)+sumOfDigit(num//10)

n=int(input("n:"))
print(sumOfDigit(n))