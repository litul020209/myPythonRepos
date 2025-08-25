
#using recursion

def gcd_of_two(p_min,q_max,gcd,i):
    #base case
    if q_max%p_min==0:
        gcd=p_min
        return gcd
    if i==min:
        return gcd
    if p_min%i==0 and q_max%i==0:
        gcd=i
        return gcd
    i=i+1
    gcd_of_two(p_min,q_max,gcd,i)
    

n = int(input("Enter the given number: "))
m=  int(input("Enter the given number: "))
x=min(n,m)
y=max(n,m)
p_min=x
q_max=y
i=1
gcd=1
# while i<=x:
#     if p_min%i==0 and q_max%i==0:
#         gcd=i
#     i=i+1
# print(gcd)
print(gcd_of_two(p_min,q_max,gcd,i))

