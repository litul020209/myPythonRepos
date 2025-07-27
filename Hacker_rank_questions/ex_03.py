n=int(input("enter the total number: "))
l=[]
for i in range(n):
    x=int(input("enter the given number "))
    l.append(x)

t=tuple(l)
print(t)

print(hash(t))