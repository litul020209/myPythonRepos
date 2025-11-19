class sample:
    a=10
    class inner:
        a1=10
        def show(self):
            print(self.a1)
            print(sample.a)
            sample.a=100

s=sample()
o=s.inner()
o.show()
print(sample.a)
print(sample.inner.a1)
