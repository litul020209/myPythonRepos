class Vehicle:
    def seat_capacity(self,seat):
        if seat==50:
            return "seating capacity of the bus is 50"
class Bus(Vehicle):
    def seat_capacity(self,seat=50):
        seats=super().seat_capacity(seat)
        return seats

obj1=Bus()
print(obj1.seat_capacity())