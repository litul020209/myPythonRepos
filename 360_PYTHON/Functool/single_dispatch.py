from functools import singledispatch as sd

@sd
def display(a,b):
    print(a,b)

@display.register(int)
def d1(a,b):
    print(f"a {a}  b {b}")

@display.register(int,float)
def d2(a,b):
    print(f"a {a} b {b}")

display(10,20.45)    #dbt