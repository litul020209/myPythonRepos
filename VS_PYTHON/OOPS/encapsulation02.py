class ATM:
    def __init__(self, pin, balance):
        self.__pin = pin
        self.__balance = balance

    def check_balance(self, entered_pin):
        if entered_pin == self.__pin:
            return f"Balance is ₹{self.__balance}"
        else:
            return "Incorrect PIN"

    def withdraw(self, entered_pin, amount):
        if entered_pin == self.__pin:
            if amount <= self.__balance:
                self.__balance -= amount
                return f"Withdrawn ₹{amount}. Remaining ₹{self.__balance}"
            else:
                return "Insufficient Balance"
        else:
            return "Incorrect PIN"

atm = ATM("4321", 5000)
print(atm.check_balance("4321"))    
print(atm.withdraw("1234", 1000))
