
class Vehicle:

   def fare_charge(self,amount,seat_capacity):
       final_charges=amount*seat_capacity
       return final_charges


class Bus(Vehicle):

    def fare_charge(self, amount, seat_capacity):
        total_fare=Vehicle.fare_charge(self,amount, seat_capacity)
        maintenance=total_fare * (1 / 10)
        return total_fare+maintenance

obj1=Bus()
print(obj1.fare_charge(100,50))

obj2=Vehicle()
print(obj2.fare_charge(100,50))


