class NumberNegativeError(Exception):
    pass
class NumberZeroError(Exception):
    pass

def take_num():
    try:
        number=int(input("Enter the number: "))
        if number <0:
            raise NumberNegativeError
        elif number==0:
            raise NumberZeroError
    except ValueError:
        print("the number should be integer!")
        take_num()
    except NumberNegativeError:
        print("The number should be non negative!")
        take_num()
    except NumberZeroError:
        print("The number should be non zero!")
        take_num()
    except:
        print(" check the logic in try block")
        take_num()
    else:
        print(number)

take_num()

