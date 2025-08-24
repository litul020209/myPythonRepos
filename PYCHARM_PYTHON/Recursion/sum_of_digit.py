
def sum_of_digit(n):
    if n==0:
        return 0
    ans=n+sum_of_digit(n-1)
    return ans

num=5
print(sum_of_digit(num))