def helper(num):
    ans=0
    l=len(str(num))
    while l!=0:
        ans=ans+(num%10)
        num=num//10
        l-=1
    return digitSum(ans)


def digitSum(num):
    if len(str(num))==1:
        return num
    else:
        return helper(num)
n=int(input("n: "))
print(digitSum(n))