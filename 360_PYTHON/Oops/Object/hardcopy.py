class sample:
    a,b,c=10,20,30
    def __init__(self,x,y):
        self.x=x
        self.y=y
        sample.a=self.x
       
    @staticmethod
    def display1():
        a=200
        return a

    def display3(self):
        print("This is the instance  method")
        print(self.a)
        print(sample.display1())

o1=sample(10,20)
o1.display3()

