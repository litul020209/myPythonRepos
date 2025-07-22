class vehicle:
    def show(self):
        print("common transport method is vehicle ")

class land_vehicle(vehicle):
    def show(self):
        print("land_surface vehicle")


class water_vehicle(vehicle):
    def show(self):
        print("water surface vehicle")


class electric_vehicle(land_vehicle,water_vehicle):
    def show(self):
        print("electric vehicle")


class fuel_vehicle(land_vehicle,water_vehicle):
    def show(self):
        print("petrol and desiel vehicle")
        vehicle.show(self)


class both_vehicle(electric_vehicle,fuel_vehicle):
    def show(self):
        print("both in electric and fuel ")

bus=fuel_vehicle()
bus.show()
print(both_vehicle.mro())
