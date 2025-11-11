class sample:
    a,b,c=10,20,30
    def __init__(self):
        self.x=100
        self.y=200
        self.z=300
    def display3(self):
        print("This is the instance  method")
        self.a=self.x,self.y,self.z,sample.a
        return self.a


obj1=sample()
print(obj1.display3())