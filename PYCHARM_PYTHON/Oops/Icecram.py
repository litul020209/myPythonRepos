
class Scoop:

    quantity_sold = 0

    def __init__(self, flavor, price):
        self.flavor = flavor
        self.__price = price


    def get_price(self):
        return self.__price


    def set_price(self, price):
        self.__price = price


    @classmethod
    def sold(cls):
        print(f"Scoop quantity sold: {cls.quantity_sold}")



class Bowl:
    def __init__(self):
        self.__scoop_list = []


    def add_scoops(self, *scoops):
        for scoop in scoops:
            self.__scoop_list.append(scoop)
            Scoop.quantity_sold += 1


    def display(self):
        total_price = 0
        print("Scoops in the bowl:")
        for scoop in self.__scoop_list:
            print(f"Flavor: {scoop.flavor}, Price: {scoop.get_price()}")
            total_price += scoop.get_price()
        print(f"Total price of bowl: {total_price}")


    def sold(self):
        print(f"Total scoops in bowl sold: {len(self.__scoop_list)}")

s1 = Scoop("Vanilla", 50)
s2 = Scoop("Chocolate", 60)
s3 = Scoop("Strawberry", 55)
bowl = Bowl()
bowl.add_scoops(s1, s2, s3)
bowl.display()
Scoop.sold()
bowl.sold()
