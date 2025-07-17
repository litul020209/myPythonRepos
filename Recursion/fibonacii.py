def fibonacii(number):
    
    if number==0:
        return 0
    elif number==1:
         return 1
    fnth=fibonacii(number-1)+fibonacii(number-2)
    return  fnth


print(fibonacii(10))