class sample:
    a=10
    b=0
    def __init__(self):
        self.x=10
    def access(self,obj):
        print(self.x)
        sample.display01(obj)

    @classmethod
    def display01(cls,obj):
        print(cls.a)
        print(sample.a)
        
        



obj1=sample()
obj1.access(obj1)
