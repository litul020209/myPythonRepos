import math as m
class fraction:
    def __init__(self,x,y=None):

        if isinstance(x, str):
            a, b = x.split("/")
            self.x = int(a)
            self.y = int(b)        
        elif isinstance(x, int) and isinstance(y, int):
            self.x = x
            self.y = y       
        else:
            raise ValueError("Invalid fraction input")


        if self.x < 0 or self.y < 0:
            if self.x < 0 and self.y < 0:
                self.x=-self.x
                self.y=-self.y
            

        if self.x==0 or self.y==0:
            if self.x==0:
                self.v=0
            elif self.y==0:
                self.v=m.inf

        elif self.x>= self.y:
            if self.x%self.y==0:
                self.value=self.x//self.y
            elif  m.gcd(self.x,self.y) != 1:
                v=m.gcd(self.x,self.y)
                self.x=self.x//v
                self.y=self.y//v 
        else:
            if  m.gcd(self.x,self.y) != 1:
                v=m.gcd(self.x,self.y)
                self.x=self.x//v
                self.y=self.y//v 
        

    def __str__(self):
        if self.x==0 or self.y==0:
            return f"{self.v}"            
        elif self.x>= self.y:
            if self.x%self.y==0:
                return f"{self.value}"
            else:
                return f"{self.x}/{self.y}"          
        else:
            return f"{self.x}/{self.y}"


    def __add__(self,other):
        self.denum=m.lcm(self.y,other.y)
        self.nume=(self.x*(self.denum//self.y))+(other.x*(self.denum//other.y))
        nume,denume=self.simplify(self.nume,self.denum)
        return fraction(nume,denume)
    

    def __sub__(self,other):
        self.denum=m.lcm(self.y,other.y)
        self.nume=(self.x*(self.denum//self.y))-(other.x*(self.denum//other.y))
        nume,denume=self.simplify(self.nume,self.denum)
        return fraction(nume,denume)
    
    def __mul__(self,other):
        self.nume=(self.x*other.x)
        self.denum=(self.y*other.y)
        nume,denume=self.simplify(self.nume,self.denum)
        return fraction(nume,denume)
    

    def __truediv__(self,other):
        self.nume=self.x*other.y
        self.denum=self.y*other.x
        nume,denume=self.simplify(self.nume,self.denum)
        return fraction(nume,denume)

    def simplify(self,nume,denum):
        self.a=nume
        self.b=denum

        if self.a < 0 or self.b < 0:
            if self.a < 0 and self.b < 0:
                self.a=-self.a
                self.b=-self.b


        if self.a>= self.b:
            if self.a%self.b==0:
                self.value=self.a//self.b
            elif  m.gcd(self.a,self.b) != 1:
                v=m.gcd(self.a,self.b)
                self.a=self.a//v
                self.b=self.b//v 
        else:
            if  m.gcd(self.a,self.b) != 1:
                v=m.gcd(self.a,self.b)
                self.a=self.a//v
                self.b=self.b//v 
        return self.a,self.b
        
f1=fraction(-1,5)
f2=fraction(1,5)
f3=fraction(2,5)
f4=f1+f2+f3
print(f4)
print(type(f4))

f7=f1-f2
print(f7)
print(type(f7))

f8=fraction(8,4)
f9=fraction(3,4)
f10=f8/f9
f11=f8/f9/f10
print(f11)
print(type(f11))

f12=f8*f9
print(f12)
print(type(f12))