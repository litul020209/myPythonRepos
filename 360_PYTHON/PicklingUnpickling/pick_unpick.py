import pickle as pi

d1="hey every one i "
print(d1,type(d1))

result=pi.dumps(d1)
print(result)
print(type(result))

result=pi.loads(result)
print(result)
print(type(result))