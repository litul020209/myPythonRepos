class sample:
    @classmethod
    def display1(cls):
        print("Class Method")
    @staticmethod
    def display():
        print("Static Method")

s=sample()
s.display1()