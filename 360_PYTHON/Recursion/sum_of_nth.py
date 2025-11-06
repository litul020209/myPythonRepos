def sumOfNth(n):
    if n==1:
        return 1
    return n+sumOfNth(n-1)
num=int(input("num: "))
print(sumOfNth(num))

