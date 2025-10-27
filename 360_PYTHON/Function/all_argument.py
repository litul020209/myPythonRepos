def display(*args):
    args=[*args]
    print(args)

display(10,20,30,40)

t1=(10,20,30,40)
t2=[*t1]

print(t2)

d1={1:10,2:20,3:30}

d2={*d1.values()}
print(d2)