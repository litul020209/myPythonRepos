class A:
    x,y,z=10,20,30

class Mymetaclass(type):
    def __new__(cls,name,bases,dct):
        print(f"name of the class {name}")
        dct={"a":10,"b":20,"c":30}
        bases=(A,)
        def display(self):
            print("Hello World")
        dct["display"]=display  #we can also form same for class and static method
        return super().__new__(cls,name,bases,dct)


class sample(metaclass=Mymetaclass):
    pass

print(dir(sample))

print(type(sample))

print(type(Mymetaclass))


s=sample()
s=Mymetaclass()
s.display()


#