class sample:
    a,b,c=10,20,30
    def __init__(self,x,y):
        self.x=x
        self.y=y
       
    @staticmethod
    def display1():
        print(sample.a)
    def display3(self):
        print("This is the instance  method")
        print(self.x,self.y)


# o1=sample(10,20)
# print(o1.display3())
print(sample.display3())