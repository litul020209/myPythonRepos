class parent:
    def __init__(self,name):
        self.name=name
        
    
    def self_01(self):
        print("Wolrld")
    
    def own(self):
        print(f"my name is {self.name}")

class child(parent):
    def self(self):
        print("Hello")
        # super().self_01()


obj_01=child("Litul")
obj_01.self()
obj_01.own()


