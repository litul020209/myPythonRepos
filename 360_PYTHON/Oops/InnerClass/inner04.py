class sample:
    a=10
    class inner:
        
        def show(self):
            print("i am in innner")

    o1=inner()

sample.o1.show()
obj1=sample()
obj1.o1.show()
obj2=sample().inner()
obj2.show()

