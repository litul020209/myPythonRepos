l_01=[2,4,7,9,4]
set_0=set(l_01)
l_01=list(l_01)
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

