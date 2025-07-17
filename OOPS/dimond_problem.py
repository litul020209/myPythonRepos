class A:
    def __init__(self,name):
        self.name=name
        self.name2=self.name.upper()
        self.name2 #you cant write return in here
        
        
    def show(self): #show 1
        print("Class A")

class a:
    def __init__(self,name):
        self.name=name
        return self.name.title()  #here we write the return but in 1st class we cant write return 
        
        
    def show(self): #show 02
        print("Class a")

class B(A,a):
    def show(self):  #show 03
        print("Class B")

class C(A):
    def show(self): #show 04
        print("Class C")

class D(B, C):
    def auto_self(self):
        print("the 1st priority")
        self.show() #this show direct to B class show
        a.show(self)
        A.show(self)
        C.show(self)
        


    

d = D("Litul")
print(D.mro())
print(d.auto_self())
str=a.__init__(d,"sonu")
str2=A.__init__(d,"monu")
print(str)
print(str2)
print(f"the name is {d.name2}  ")
