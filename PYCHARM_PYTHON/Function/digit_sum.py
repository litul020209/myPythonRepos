def digit_sum(num):
    sum=0
    for i in range(1,num+1):
        sum+=i
    return sum
n=int(input("enter the number: "))
print(digit_sum(n))