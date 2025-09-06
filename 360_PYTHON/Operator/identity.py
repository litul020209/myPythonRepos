a=30
b=30
print(a is b)
print(b is a)

a=30
b=5*6
print(a is b)

a=30
b=a
c=b
print(a is c)


a=0
b=False

print(a is b)

a=[1,2,3]
b=[1,2,3]
print(a is b)

# "==" compare the value but is compare the memory statement

a="str"
b="str"
print(a is b)

a="A123"
b="A123"
print(a is b)

a=1.2
b=1.2
print(a is b)

a=2+2j
b=2+2j
print(a is b)

a="2+3j"
b="2+3j"
print(a is b)

a=300
b=300
print(a is b)


a=2+3j
b=2+3j
print(a,id(a))

print(b,id(b))

print(a is b)


c = complex(2, 3)
d = complex(2, 3)
print(c is d)   