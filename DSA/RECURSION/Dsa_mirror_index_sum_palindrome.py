
def reverse_num(num,num2=0):   
      
    if  num!=0:
        digit=num%10
        num2=(num2*10)+digit
        num=num//10
        return reverse_num(num,num2)
    else:
        return num2

def mirror_palindrome(num,steps):
    num1=reverse_num(num)
    res=num+num1
    res1=reverse_num(res)
    if res==res1:
        return steps
    else:
        steps+=1
        return mirror_palindrome(res,steps)
       
num=int(input("Enter the number: "))
steps=1
ans=mirror_palindrome(num,steps)
print(ans)

