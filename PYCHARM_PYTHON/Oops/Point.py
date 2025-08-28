class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Location:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    def reflect_on_x_axis(self):

        reflected = Point(self.destination.x, -self.destination.y)
        print(f"Reflection of Destination on X-axis: ({reflected.x}, {reflected.y})")


source = Point(2, 3)
destination = Point(5, 7)

loc = Location(source, destination)
loc.reflect_on_x_axis()
