
def find_digit(n):
    if n//10==0:
        return 1
    small=find_digit(n//10)
    ans=1+small
    return ans

n=int(input("enter the number: "))
print(find_digit(n))