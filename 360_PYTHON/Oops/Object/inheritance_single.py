class sample:
    a,b=10,20
    def __init__(self):
        self.x=10

class sample2:
    def display(self,obj):
        print("inside sample2")
        obj.__init__(self)

        
        
obj1=sample()
obj2=sample2()
print(obj2.display(obj1))
print(obj2.obj1.x)

