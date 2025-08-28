f
class Polygon:
    def __init__(self):
        pass
    def dimension(self):
        

class Triangle(Polygon):
   def area(self):
       pass

   def dimension(self):
       Polygon.dimension()

class Rectangle(Polygon):
    def area(self):
        pass
    def dimension(self):
        Polygon.dimension()