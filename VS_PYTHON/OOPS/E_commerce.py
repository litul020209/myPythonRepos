class User:
    def __init__(self,name,mail):
        self.name=name
        self.mail=mail
    
class Customer(User):
    def __init__(self, name, mail):
        super().__init__(name, mail)
    def cart():
        pass
    def order():
        pass

class PrimeCustomer(Customer):
       def __init__(self, name, mail,):
           super().__init__(name, mail)
      
       def MemberShip():
           pass
       def CashBack_percentage():
           pass
       def LoyalityPoints():
           pass

