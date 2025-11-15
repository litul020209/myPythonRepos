def geoMetric(start,ratio,num,ans):
    if num!=0:
        number=start*(ratio**(num-1))
        
        ans=ans+number
        geoMetric(start,ratio,num-1,ans)
        print(number)
    else:
        print(ans)    

s=int(input("s: "))
n=int(input("n: "))
r=int(input("r: "))
res=0
geoMetric(s,r,n,res)