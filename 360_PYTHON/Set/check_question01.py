a = {10, 20, 30}
b = {30, 40, 50}
print(a ^ b)

a = {1, 2, 3}
b = {1, 2, 3}
print(a is b)

a=4
b=a
print(id(a),id(b))
a=a+4

print(id(a),id(b))
