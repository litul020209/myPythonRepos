
class Rectangle:
    def __init__(self):
        self.length=0
        self.height=0
    def area(self):
        return self.length*self.height
    def is_square(self):
        value="Square" if self.length==self.height else "Not a Square"
        return value
obj=Rectangle()
obj.length=12
obj.height=12
area=obj.area()
print("area is :",area)
print(obj.is_square())
