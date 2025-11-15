class sample:
    a,b=10,20
    @classmethod
    def ab(cls):
        print("abc")
    @staticmethod
    def ab():
        print("def")


obj1=sample()
obj1.ab()
    