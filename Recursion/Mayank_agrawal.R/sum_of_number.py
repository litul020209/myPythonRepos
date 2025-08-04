def sumNum(num):
    if num//10==0:
        return num
  
    smallans=num%10
    ans=smallans+sumNum(num//10)
    return ans



num=int(input("enter the number: "))
print(sumNum(num))