ans=""
def binaryNumber(num,str1):
    global ans
    if num==2 or num==3:
       a=num%2
       b=num//2
       astr=str(a)
       bstr=str(b)
       str1=astr+str1
       str1=bstr+str1
       return str1
    sans=num%2
    ans=str(sans)
    str1=ans+str1
    num=num//2
    return binaryNumber(num,str1)

num=15
str1=""
print(f"binary number of 5 is :{binaryNumber(num,str1)}")