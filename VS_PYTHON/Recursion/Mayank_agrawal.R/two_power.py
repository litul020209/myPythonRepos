
def two_p(n):
    if n==0:
        return 1
    smllAns=2**(n-1)
    ans=2*smllAns
    return ans

    

n=int(input("enter the power of 2 : "))
print(two_p(n))

