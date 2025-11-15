class sample:
    __a,__b,c=10,20,30
    def __init__(self):
        self.__x=int(input("x: "))
        self.__y=int(input("y: "))
        
       
  
    def display1(self):
        return self.__x,self.__y
class sample2(sample):
    def __init__(self):
        super().__init__()() 
s1=sample()
print(s1.display1())
    
       
