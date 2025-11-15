def arithmatic_series(a,d,n,ans):
    if n!=0:
        if n==4:
            a=a
        else:
            a=a+3
        print(a)
        ans=ans+a
        arithmatic_series(a,d,n-1,ans)
    else:
        print(ans)


a=int(input("a: "))
d=int(input("d: "))
n=int(input("n: "))
res=0
arithmatic_series(a,d,n,res)