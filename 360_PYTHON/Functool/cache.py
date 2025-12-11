from functools import cache

@cache
def cube(a):
    print("inside the function")
    return a**3

# you can't control the max size in cache , its by defult none .


