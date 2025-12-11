from functools import lru_cache

@lru_cache
def cube(a):
    print("inside the function")
    return a**3

print(cube(2))
print(cube(3))
print(cube(4))
print(cube(3))

print(cube.cache_info())


@lru_cache(max=10)
def cube(a):
    print("inside the function")
    return a**3

print(cube(2))
print(cube(3))
print(cube(4))
print(cube(3))
print(cube.cache_info())



