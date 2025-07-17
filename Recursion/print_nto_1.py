def number_0_to_n(number):
    n=number
    if n==1:
        return 1
    print(n)
    return number_0_to_n(n-1) 


def one_to_n_print(number):
    n=number
    if n==0:
       return 0
    one_to_n_print(n-1)
    print(n)

num1=number_0_to_n(10)
print(num1)
print("  ")
num2=one_to_n_print(10)
print(num2)
     
       
     
