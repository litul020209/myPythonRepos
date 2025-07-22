class Person:
    def __init__(self, name, age):
        self.name = name            # public
        self.__age = age            # private

    def display(self):
        print(f"Name: {self.name}, Age: {self.__age}")

p = Person("Alice", 30)
p.display()
print(dir(p)) #using dir you find all name mangling
print(p._Person__age)  #using name mangling _Person__age