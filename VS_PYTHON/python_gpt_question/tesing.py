x = 256
y = 256
print(x is y)  # True (interned integers)

a = 257
b = 257
print(a is b)  # False (different memory objects)
