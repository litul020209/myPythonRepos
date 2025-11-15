class sample:
    __a,__b,c=10,20,30
    # def __init__(self,x,y):
    #     self.x=x
    #     self.y=y
    #     sample.a=self.x
       
  
    def display1(self):
        
        return sample.__a

    def __display3(self):
        return 20
       

obj=sample()
print(dir(obj))
obj._sample__a=1000
print(obj._sample__a)
print(obj._sample__display3())
print(obj.display1())