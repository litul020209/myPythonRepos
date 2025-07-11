def prime(x):
    count=0
    for i in  range(1,x+1):
        if x%i==0:
            count=count+1
    if count==2:
                print("the number is a prime number",x)
    else:
                print("the number is no a prime number",x)     

def armstrong(x):
       y=str(x)
       l=len(y)
       n4=0
       for n1 in y:
           n2=int(n1)
           n3=n2**l
           n4=n4+n3
       x=int(y)
       if x==n4:
           print("the number is a armstrong number",x)
       else:
           print("the number is not a armstrong number",x)


def palindrome(x):
      y=str(x)
    #   z="".join(reversed(y)) #it can also reverse the string
      z=y[::-1]
      if y==z:
            print("the number is palindrome number",x)
      else:
            print("the number is not a palindrome number",x)

a=int(input("enter the number: "))
prime(a)
armstrong(a)
palindrome(a)
            
