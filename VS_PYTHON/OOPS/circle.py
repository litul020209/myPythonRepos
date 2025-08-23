class circle:
    def __init__(self,radius):
        self.r=radius
    def area(self):
        return 3.141*self.r*self.r
    def circumstances(self):
        return 2*3.141*self.r
    
circle_01=circle(5)
print(f"area of circle is {circle_01.area()}")
print(f"circumstances of circle is {circle_01.circumstances()}")
        