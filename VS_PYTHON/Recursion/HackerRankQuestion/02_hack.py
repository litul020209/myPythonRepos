def find_power(m,n):
    if n==0:
        return 1
    sans=find_power(m,n-1)
    ans=sans*m
    return ans
    
m=int(input("m base: "))
n=int(input("n exp: "))
print(find_power(m,n))