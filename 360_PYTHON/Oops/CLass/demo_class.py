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
    @classmethod
    def display3(cls):
        return 10
        

o1=sample(10,20)
print(o1.display3())