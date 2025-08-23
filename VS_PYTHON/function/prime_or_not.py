

def prime_or_not(*number):
    
    for n in number:
        count=0
        for i in range(1,n+1):
            if n%i==0:
               count+=1
        if count<=2:
            print(f"the {n} is a prime nunmber")
        else:
            print(f"the {n} is not a prime number") 
    

number_1=int(input("enter the number: "))
number_2=int(input("enter the number: "))
number_3=int(input("enter the number: "))

prime_or_not(number_1,number_2,number_3)
            