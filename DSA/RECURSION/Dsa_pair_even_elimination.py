def evevn_pair_eliminated(num):

    length=0
    num_list=[]

    for x in f"{num}":
        length+=1
    x=length
    ans=num
    while x!=0:
        digit=num//10**(x-1)
        num_list+=[digit]
        num=num-(digit*(10**(x-1)))
        x-=1
    
    p=0
    q=1
    
    res=0
    while q < length:
        if (num_list[p]+num_list[q])%2 !=0:
            res=(res*10)+num_list[p]
            if q==(length-1):
                res=(res*10)+num_list[q]
            p=q
            q=q+1

        else:
            p=p+1
            q=q+1

    if res==ans:
        return ans
    else:
        return  evevn_pair_eliminated(res)
    

num=int(input("num: "))
print(evevn_pair_eliminated(num))