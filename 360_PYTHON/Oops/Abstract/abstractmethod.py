from abc import abstractclassmethod,ABC
class sample(ABC):
    
    @classmethod
    @abstractclassmethod
    def display(cls):
        pass

    @abstractclassmethod    #same for static method also
    def display2(self):
        pass

class sample2(sample):
    @classmethod
    def display(cls):
        print("SAMPLE2")

    def display2(self):
        print("sample2")

s1=sample2()
s1.display2()
s1.display()