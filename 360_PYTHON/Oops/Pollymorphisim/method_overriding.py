class A:
    def a(self):
        print("A")

class B(A):
    def a(self):
        print("B")

class C(B):
    def a(self):
        A.a(self)
        super().a()
        print("C")
        
        

obj=C()
obj.a()


