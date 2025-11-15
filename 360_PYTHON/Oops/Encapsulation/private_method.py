class sample:
    __a,__b,c=10,20,30
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.__z=500
       
  
    def display1(self):
        print(sample.__a)
        return sample.__a,self.__z

    def __display3(self):
        return 20
       
class sample2(sample):
    def sample_paper():
        print("Hello Boy")
# obj=sample(90,80)
# print(dir(obj))
# sample._sample__a=1000
# print(obj.display1())
# print()