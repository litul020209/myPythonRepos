import math as m

class Fraction:
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
        return Fraction(num, den)

    def __sub__(self, other):
        num = self.x * other.y - other.x * self.y
        den = self.y * other.y
        return Fraction(num, den)

    def __mul__(self, other):
        num = self.x * other.x
        den = self.y * other.y
        return Fraction(num, den)

    def __truediv__(self, other):
        num = self.x * other.y
        den = self.y * other.x
        return Fraction(num, den)
    


f1=Fraction(input("f1: "))
f2=Fraction(input("f2: "))
f3=Fraction(input("f2: "))

print(f"{f1} + {f2} + {f3} is {f1+f2}")
print(f"{f1} * {f2} * {f3} is {f1*f2*f3}")