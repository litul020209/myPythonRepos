from abc import ABC,abstractmethod

class payment(ABC):
    def __init__(self):
        self.total_balance=1000
    @abstractmethod
    def deposite(self,amount):
        pass
    @abstractmethod
    def withdraw(self,amount):
        pass

class crediCard(payment):
    def __init__(self):
         payment.__init__(self)

    def deposite(self, amount):
        super().deposite(amount)
        self.deposite=amount
        print(f"your deposite amount is {self.deposite}")
        print(f"total balance is {self.total_balance+self.deposite} amount")
        print("thanks for using creditCard payment system")
    
    def withdraw(self, amount):
        super().withdraw(amount)
        self.withdraw=amount
        if self.withdraw>self.total_balance:
               print("you have not that much of amount in your bank account")
               print("Thanks for coming")
               return
               
        else:      
               print(f"your with draw amount is {self.withdraw}")
               print(f"total balance is {self.total_balance-self.withdraw} amount")
               print("thanks for using creditCard payment system")

class debitCard(payment):
    def __init__(self):
         payment.__init__(self)
    def deposite(self, amount):
        super().deposite(amount)
        self.deposite=amount
        print(f"your deposite amount is {self.deposite}")
        print(f"total balance is {self.total_balance+self.deposite} amount")
        print("thanks for using debitcard payment system")
    
    def withdraw(self, amount):
        super().withdraw(amount)
        self.withdraw=amount
        if self.withdraw>self.total_balance:
                print("you have not that much of amount in your bank account")
                print("Thanks for coming")
                return
               
        else:
               print(f"your with draw amount is {self.withdraw}")
               print(f"total balance is {self.total_balance-self.withdraw} amount")
               print("thanks for using debitcard payment system")

class upi(payment):
    def __init__(self):
         payment.__init__(self)
    def deposite(self, amount):
        super().deposite(amount)
        self.deposite=amount
        print(f"your deposite amount is {self.deposite}")
        print(f"total balance is {self.total_balance+self.deposite} amount")
        print("thanks for using upi payment system")
    
    def withdraw(self, amount):
        super().withdraw(amount)
        self.withdraw=amount
        if self.withdraw>self.total_balance:
               print("you have not that much of amount in your bank account")
               print("Thanks for coming")
               return
        else:
               print(f"your with draw amount is {self.withdraw}")
               print(f"total balance is {self.total_balance-self.withdraw} amount")
               print("thanks for using upi payment system")

payment_method=input("enter your payment method (upi/debitcard/creditcard),\nplease give no space when you writing this may be show you error so be carefilly : ")
payment_method=payment_method.lower()


if payment_method=="debitcard":
     user_01=debitCard()
     bank_transaction=input("enter your banking method (deposite/withdraw): ")
     if bank_transaction=="deposite":
          amount=int(input("enter your deposite amount: "))
          user_01.deposite(amount)
     else:
          amount=int(input("enter your withdraw amount: "))
          user_01.withdraw(amount)

elif payment_method=="creditcard":
     user_01=crediCard()
     bank_transaction=input("enter your banking method (deposite/withdraw): ")
     if bank_transaction=="deposite":
          amount=int(input("enter your deposite amount: "))
          user_01.deposite(amount)
     else:
          amount=int(input("enter your withdraw amount: "))
          user_01.withdraw(amount)
          
else:
     user_01=upi()
     bank_transaction=input("enter your banking method (deposite/withdraw): ")
     if bank_transaction=="deposite":
          amount=int(input("enter your deposite amount: "))
          user_01.deposite(amount)
     else:
          amount=int(input("enter your withdraw amount: "))
          user_01.withdraw(amount)
          
     