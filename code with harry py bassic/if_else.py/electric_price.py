x=int(input("enter the number:"))
if x<=100:
    print("the electric price is 0")
elif x>100 and  x<=200:
   price=x*5 
   print("the price of electric bill is :",price)
else: 
    y=x-100
    z=y-100
    price=(100*5)+(z*10)
    print("the price of electric bill is :",price)    