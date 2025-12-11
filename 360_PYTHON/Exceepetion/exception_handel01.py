def handel_01():
    try:
        a=int(input("a: "))
        b=int(input("b: "))
    except:
        print("please give correct input for  a ,b !")
        handel_01()

    else:

        print(a-(-b))

    

handel_01()
