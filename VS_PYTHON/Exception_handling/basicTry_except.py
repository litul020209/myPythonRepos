
try:
    num=100
    dnum=0
    print(num/dnum)
except:
    print("error occured")  #this is basic syntax


num=100
try:
    dnum=int(input("enter the denomenator: "))
    print(num/dnum)
except  ZeroDivisionError as e:
    print("pls dont enter 0")

print("out side ")

