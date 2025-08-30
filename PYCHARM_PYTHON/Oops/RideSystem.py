# Base Ride class
class Ride:
    def __init__(self, start, end, distance, driver, customer):
        self.start = start
        self.end = end
        self.distance = distance
        self.driver = driver
        self.customer = customer

    def calculate_fare(self):
        """Default fare calculation (can be overridden by subclasses)."""
        return self.distance * 10  # base rate ₹10 per km

    def ride_details(self):
        return f"Ride from {self.start} to {self.end}, Distance: {self.distance} km"


# Subclasses with overridden fare rules
class CarRide(Ride):
    def calculate_fare(self):
        return self.distance * 15  # ₹15 per km for car


class BikeRide(Ride):
    def calculate_fare(self):
        return self.distance * 8  # ₹8 per km for bike


class AutoRide(Ride):
    def calculate_fare(self):
        return self.distance * 12  # ₹12 per km for auto


# Driver class
class Driver:
    def __init__(self, name, vehicle):
        self.name = name
        self.vehicle = vehicle

    def __str__(self):
        return f"Driver {self.name} ({self.vehicle})"


# Customer class
class Customer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Customer {self.name}"


d1 = Driver("Ramesh", "Car")
d2 = Driver("Suresh", "Bike")
d3 = Driver("Mahesh", "Auto")

c1 = Customer("Amit")

ride1 = CarRide("Station", "Airport", 10, d1, c1)
ride2 = BikeRide("Market", "College", 5, d2, c1)
ride3 = AutoRide("Mall", "Home", 8, d3, c1)

print(ride1.ride_details(), "| Fare:", ride1.calculate_fare(), "|", ride1.driver, "|", ride1.customer)
print(ride2.ride_details(), "| Fare:", ride2.calculate_fare(), "|", ride2.driver, "|", ride2.customer)
print(ride3.ride_details(), "| Fare:", ride3.calculate_fare(), "|", ride3.driver, "|", ride3.customer)