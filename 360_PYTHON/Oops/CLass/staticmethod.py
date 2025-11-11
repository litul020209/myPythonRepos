class sample:
    a,b,c=10,20,30
    def __init__(self):
        self.x=100
        self.y=200
        self.z=300
    @staticmethod
    def display1():
        print(sample.a)
    def display3(self):
        print("This is the instance  method")

# sample.display1()
# o1=sample()
# print(o1.a)
# print(o1.display3())

print(sample.display3(2))

