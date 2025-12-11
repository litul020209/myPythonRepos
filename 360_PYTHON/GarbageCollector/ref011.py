import sys
a=10
b=20
c=30
print(sys.getrefcount(a))
print(sys.getrefcount(b))
print(sys.getrefcount(c))
a1=10
b1=20
c1=30
print(sys.getrefcount(a))
print(sys.getrefcount(b))
print(sys.getrefcount(c))