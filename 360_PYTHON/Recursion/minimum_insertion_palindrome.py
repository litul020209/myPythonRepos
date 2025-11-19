def minimium_step(str1,ans):
    len=0
    for  i in str1:
        len+=1
    if len!=1:
        if str1[0]!=str1[len-1]:
            ans+=1
            minimium_step(str1[1:],ans)
        else:
            minimium_step(str1[1:(len-1)],ans)
    else:
        print(ans)
    

str1=input("str1: ")
ans=0
minimium_step(str1,ans)