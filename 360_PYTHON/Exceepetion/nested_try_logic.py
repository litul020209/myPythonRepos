try:
    a=int(input("a: "))
    if a < 10:
        try:
            if a > 5:
                raise ValueError
           
        except ValueError:
            print("a is greater than 5")
        except:
            print("check the inner try logic")
        else:
            print(a)
except:
    print("The outer check  have some problem")
else:
    print(a)