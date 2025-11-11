class sample:
    a,b,c=10,20,30
    @classmethod
    def display1(cls):
        print("Hello World")
        # print(sample.a)
        # print(cls.a)
        # sample.a=20
        # cls.a=30
        # print(cls.a)
        sample.display02()
    @staticmethod
    def display02():
        print("Hello Hyderbad")

# print(sample.a)
# sample.a=30
# print(sample.a) #we manipulate the class data using class keyword

sample.display1()


