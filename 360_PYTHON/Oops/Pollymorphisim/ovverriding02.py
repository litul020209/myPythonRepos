class sample:
    def display(self):
        print("this is sample method")
    def add(self,a,b):
        print(a+b)
class sample2(sample):
    def add(self,a,b):
        print(a*b)

s=sample2()
s.add(10,20)

s=sample()
s.add(10,20)