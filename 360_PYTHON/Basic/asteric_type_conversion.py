a="1234"


a=[*a]
print(a)



a=(*a,)
print(a)


a={*a}
print(a)

b={1:10,2:20,3:30}
b={**b}

print(b)

c={*b}
print(*c)

d={*b.keys()}
print(*d)

v={*b.values()}
print(*v)


