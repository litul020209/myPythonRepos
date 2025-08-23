
def perfectNumber(num):
    ans=[]
    for i in range(1,num):
        if num%i==0:
            ans.append(i)
    res=sum(ans)
    if res==num:
        return True
    else:
        return False

num=6
ans_out=perfectNumber(num)
print(ans_out)
