def expansion(num,length,ans):
    if length!=0:
        d1=num//10**(length-1)
        if d1%2==0:
            d2=d1//2
            if not ans:
               ans=f"{d1}{d2}"
              
            else:
               ans=ans+f"{d1}{d2}"
        else:
            d1=d1*d1
            if not ans:
               ans=f"{d1}"
            else:
               ans=ans+f"{d1}"
        num=num-(d1*(10**(length-1)))
        expansion(num,length-1,ans)
    else:
        print(ans)

            
num=int(input("num: "))
if num<0:
    num=-num
ans=""
length=0
for i in f"{num}":
    length+=1

expansion(num,length,ans)