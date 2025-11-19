class sample:
    def __init__(self):
        self.__a=10
    @property
    def a(self):
        return self.__a
    @a.setter
    def a(self,a):
        self.__a=a

s=sample()
print(s.a)
s.a=100
print(s.a)