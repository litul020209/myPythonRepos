l_01=[1,5,4,6,3,7,8,2,9]
a=True
while a==True:
    Swap=False
    p=0
    n=len(l_01)-1
    for i in range(n):
        if l_01[p]>=l_01[p+1]:
            m=l_01[p+1]
            l_01[p+1]=l_01[p]
            l_01[p]=m
            p=p+1
            Swap=True
        else:
            p=p+1
    if not Swap:
        break
        
    n=n-1
print(l_01)

