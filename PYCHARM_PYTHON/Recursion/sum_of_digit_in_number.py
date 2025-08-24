
def sum_of_digit(n,s1):
    if n<10:
        s1= s1 + n
        return s1
    else:
        r=n%10
        s1+=r
        return sum_of_digit(n // 10, s1)

num =9990
s=0
print(sum_of_digit(num,s))