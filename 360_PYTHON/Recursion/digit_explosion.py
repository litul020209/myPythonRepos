def explosion(num,len,ans):
    if len!=0:
       d=num//10**(len-1)
       w=f"{d}"*d
       if not ans:
           ans=w
       else:
           ans=ans+w
       num=num-(d*(10**(len-1)))
       explosion(num,len-1,ans)
    else:
        print(ans)

num=int(input("num: "))
len=0
for i in f"{num}":
    len+=1
ans=""
explosion(num,len,ans)

