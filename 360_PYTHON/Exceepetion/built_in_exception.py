class NumberNegativeError(Exception):
    pass
class NumberZeroError(Exception):
    pass

try:
    number=int(input("Enter the number: "))
    if number <0:
        raise NumberNegativeError
    elif number==0:
        raise NumberZeroError
except ValueError:
    print("the number should be integer!")
except NumberNegativeError:
    print("The number should be non negative!")
except NumberZeroError:
    print("The number should be non zero!")
except:
    print(" check the logic in try block")
else:
    print(number)