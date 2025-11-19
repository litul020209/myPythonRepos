class sample:
    def __init__(self):
        self.__a=10
    def get_a(self):
        return self.__a
    def set_a(self,a):
        self.__a=a
    


s1=sample()
print(s1.get_a())
s1.set_a(100)
print(s1.get_a())
print(s1._sample__a)
print(dir(s1))