import math as m

class fraction:
    def __init__(self, x, y=None):
       
        if isinstance(x, str):
            a, b = x.split("/")
            self.x = int(a)
            self.y = int(b)

        
        elif isinstance(x, int) and isinstance(y, int):
            self.x = x
            self.y = y

        else:
            raise ValueError("Invalid fraction input")

        
        if self.y == 0:
            self.x = 1
            self.y = 0
            return

        
        if self.y < 0:
            self.x = -self.x
            self.y = -self.y

    
        g = m.gcd(self.x, self.y)
        self.x //= g
        self.y //= g

    def __str__(self):
        if self.y == 1:
            return str(self.x)
        if self.y == 0:
            return "inf"
        return f"{self.x}/{self.y}"

    def __add__(self, other):
        num = self.x * other.y + other.x * self.y
        den = self.y * other.y
        return fraction(num, den)

    def __sub__(self, other):
        num = self.x * other.y - other.x * self.y
        den = self.y * other.y
        return fraction(num, den)

    def __mul__(self, other):
        num = self.x * other.x
        den = self.y * other.y
        return fraction(num, den)

    def __truediv__(self, other):
        num = self.x * other.y
        den = self.y * other.x
        return fraction(num, den)
    

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

f100=fraction(input("f100: "))
print(f100)

f101=fraction(input("f101: "))
print(f101)

