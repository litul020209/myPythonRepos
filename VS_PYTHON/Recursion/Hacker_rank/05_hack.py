def toh(n,a=1,b=2,c=3):
    if n==1:
        print((a,c))
        return
    toh(n-1,a,c,b)
    print((a,c))
    toh(n-1,b,a,c)

toh(3)