from abc import ABC,abstractclassmethod
class Resturant:
    def __init__(self):
        self.menu_price={}
        self.resturant_location="Hyderbad"
    def menu_list(self):
        self.menulist=[k for k in self.menu_price ]
        print(self.menulist)


class Food(Resturant):
    def __init__(self):
        super().__init__()
        

class DeliveryBoy:
    def __init__(self,name,dl,location):
        self.name=name
        self.dl=dl
        self.delivery_boy_location=location
        

class Order(Resturant,ABC):
    def __init__(self):
        super().__init__()
        self.customer=Customer()


    def generate_bill(self):
        pass


class HomeOrder(Order):
    def generate_bill(self):
        pass
    

class TakeawayOrder(Order):
    def generate_bill(self):
        pass


class Customer:
    def __init__(self,name,location):
        self.destin=location
        self.name=name
        self.food=Food()
    def menu(self):
        resturant_menue= self.food.menu_list()
        return resturant_menue
    
    def my_list(self,*items):
        self.my_item=list(items)

    def order(self):
        self.order=Order(self.my_item)






