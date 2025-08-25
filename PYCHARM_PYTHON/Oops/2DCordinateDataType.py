import math
from sympy import symbols, Eq, simplify

class coordinate:
    def __init__(self,a,b):
        self.x=a
        self.y=b
    def __str__(self):
        return f"({self.x},{self.y})"
    def distance(self,other):
        d=((self.x-other.x)**2 + (self.y-other.y)**2)
        return math.sqrt(d)
    def point_on_line(self,equation):
        x=self.x
        y=self.y
        res=eval(equation)
        if abs(res) < 1e-9:
            print( "point in the line")
        else:
            print("point not in the line")
    def distance_from_line(self,equation):
        x, y = symbols('x y')
        expr = simplify(equation)
        a = expr.coeff(x)
        b = expr.coeff(y)
        c = expr.subs({x: 0, y: 0})
        x=self.x
        y=self.y
        numerator=eval(equation)
        numerator=abs(numerator)
        denominator=math.sqrt(a**2 + b**2)
        result=numerator/denominator
        res=round(result,3)
        print(res)

obj1=coordinate(3,4)
obj2=coordinate(1,-1)
eq="2*x + 3*y + 6"
obj1.point_on_line(eq)
obj2.distance_from_line(eq)
