def prime(n,m):
    if n%m==0:
        return False
    if (n-1)==(m):
        return True
    return prime(n,m+1)
    

print(prime(12,2))