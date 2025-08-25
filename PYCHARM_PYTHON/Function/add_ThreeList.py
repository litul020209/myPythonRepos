import functools
def add(*args):
    summ = 0
    for x in args:
        s=functools.reduce(lambda a,b: a+b,x)
        summ+=s
    return summ

arr1=[2,5,8,9]
arr2=[1,6,9,5,7]
arr3=[3,9,7,0,5]

print(add(arr1,arr2,arr3))