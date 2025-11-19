class sample:
    a=10
    class inner:
        a1=100
        @classmethod
        def show(cls):
            print(cls.a1)
            print(sample.a)

s=sample()
o1=s.inner()
o1.show()
print(sample.inner.a1)
print(sample.inner.a1) 