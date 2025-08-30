class Product:
    __product_id = 0

    def __init__(self, name, price):
        Product.__product_id += 1
        self.productid = Product.__product_id
        self.__name = name
        self.__price = price

    def set_name(self, value):
        self.__name = value
        return self.__name

    def set_price(self, value):
        self.__price = value
        return self.__price

    def get_price(self):
        return self.__price

    def get_details(self):
        return {
            "id": self.productid,
            "name": self.__name,
            "price": self.__price
        }

class Cart:
    def __init__(self):
        self.products = []

    def add(self, p):
        self.products.append(p)

    def remove_product(self, product_id):
        new_list = []
        for p in self.products:
            if p.productid != product_id:
                new_list.append(p)
        self.products = new_list

    def checkout(self):
        total = 0
        for product in self.products:
            total += product.get_price()
        return total

p1 = Product("Chocolate", 50)
p2 = Product("Milk", 30)
p3 = Product("Bread", 40)
cart = Cart()
cart.add(p1)
cart.add(p2)
cart.add(p3)
print("Total Bill:", cart.checkout())
cart.remove_product(2)
print("Total Bill after removing Milk:", cart.checkout())  # should print 90
