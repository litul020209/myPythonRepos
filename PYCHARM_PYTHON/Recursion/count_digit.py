
def count_digit(n,ans):
    if n<10:
        ans+=1
        return ans
    else:
        ans+=1
        return count_digit(n//10,ans)

num=1234000
a=0
print(count_digit(num,a))
