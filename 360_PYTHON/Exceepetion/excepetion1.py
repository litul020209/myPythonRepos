try:
    a=int(input("a: "))
    b=int(input("b: "))
except:
    print("please give correct input for  a ,b !")

else:

    print(a-(-b))

finally:
    print("finally I am the boss")