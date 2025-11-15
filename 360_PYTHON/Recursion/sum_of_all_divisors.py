def sum_of_all_divisors(num,n,ans):

    if n!=num+1:
        if num%n==0:
            ans+=n
        sum_of_all_divisors(num,n+1,ans)
        
    else:
        print(ans)

n=1
num=int(input("num: "))
ans=0
sum_of_all_divisors(num,n,ans)