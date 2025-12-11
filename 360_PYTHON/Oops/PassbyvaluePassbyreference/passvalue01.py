
a=10
class Person:
    def value(self,x):
        print(id(x))
        x=20
        

p=Person()
p.value(a)
print(id(a))
print(a)




