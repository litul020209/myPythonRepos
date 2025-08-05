nums = [-4,-1,0,3,10]
snum=[]

for x in nums:
    x=abs(x)
    y=x**2
    snum.append(y)

snum.sort()
print(snum)