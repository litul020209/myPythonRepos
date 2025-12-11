from collections import defaultdict as dd

d1=dd(int)

d1["a"]="Hello"

print(dict(d1))
print(d1["b"])

d1=dd(str)
d1["a"]=1
print(d1["b"],type(d1["b"]))