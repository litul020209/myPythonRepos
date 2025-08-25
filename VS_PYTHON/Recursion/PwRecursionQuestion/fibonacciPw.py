
# def fibo_nth(n):
#     if n==1 or n==0:
#         return n
#     return fibo_nth(n-1)+fibo_nth(n-2)

# print("\n")

def fibonacci(n,f1,f2,f):             #using while loop method
    if n==0:
        return 
    f=f1+f2
    print(f,end=" ")
    f1=f2
    f2=f
    fibonacci(n-1,f1,f2,f)

# print("\n")    
#using while loop
f1=0
f2=1
f=0
n=int(input("enter the number : "))
print(fibonacci(n,f1,f2,f))
# while n>0:
#      f=f1+f2
#      print(f,end=" ")
#      f1=f2
#      f2=f
#      n=n-1


# for i in range(n):
#     print(fibo_nth(i),end=" ")

# print(fibo_nth(n))                              