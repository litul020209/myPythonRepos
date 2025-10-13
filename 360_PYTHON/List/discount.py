actual = [100,200,400]
sold = [90,160,300]
ans=[]
for i in range (len(sold)):
    p1=actual[i]
    p2=sold[i]
    if p1 > p2:
        p1,p2=p2,p1
    discount=(p2-p1)/actual[i]
    print(discount)
    discount_=discount*100
    print(discount_)
    ans.append(discount_)
print(ans)
