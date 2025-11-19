class sample:
    a=10
    class inner:
        a1=100
        
        def __init__(self):
            self.a1=int(input("a1: "))
            print(self.a1)
            print(sample.a)


s=sample()
o1=s.inner()
print(o1.a1)
o1.a1=200
print(o1.a1)

