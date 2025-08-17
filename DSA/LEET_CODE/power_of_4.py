def power(num):
    if num<=0:
        return False
    if num==1:
        return True
    num=num/4
    if num==1:
        return True
    if num%4==0:
        
        ans= power(num)
    else:
        ans= False
    return ans


num=17
print(power(num))