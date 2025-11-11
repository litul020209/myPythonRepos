class sample:
    a=10
    b=0
    def __init__(self):
        self.x=int(input("Enter a: "))
    def __str__(self):
        return f"{self.x} and {sample.a}"
    def display01(self):
        print(f"{self.x}")

obj1=sample()
print(obj1.display01())
print(str(obj1))

