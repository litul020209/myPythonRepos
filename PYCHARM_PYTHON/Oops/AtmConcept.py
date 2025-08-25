class ATM:
    def __init__(self, enter=None, name="Litul Biswal", Acc_num=1234):
        self.balance = 10000
        self.enter = enter
        self.name = name
        self.acc_num = Acc_num
        self.pin = "1111"

        if self.enter == 4:
            self.pin_generate()
        else:
            pin = input("Enter your pin: ")

            if self.pin == pin:
                while True:
                    print("\n1 for check balance")
                    print("2 for deposit balance")
                    print("3 for withdrawal balance")
                    print("4 for pin generate/change")
                    print("5 for account details")
                    print("6 for exit")
                    choice = int(input("Enter your choice: "))

                    if choice == 1:
                        self.check_balance()
                    elif choice == 2:
                        self.deposite()
                    elif choice == 3:
                        self.withdraw()
                    elif choice == 4:
                        self.pin_generate()
                    elif choice == 5:
                        self.details()
                    elif choice == 6:
                        print("Thank you! Please take your card.")
                        break
                    else:
                        print("Invalid choice")

    def pin_generate(self):
        self.new_pin = input("Enter the pin number (4 digits): ")
        self.pin = self.new_pin

    def check_balance(self):
        print(f"Your balance is {self.balance}")
        input("Press Enter to continue...")

    def deposite(self):
        amount = int(input("Enter your deposit amount: "))
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self):
        amount = int(input("Enter your withdraw amount: "))
        if amount > self.balance:
            print("You don't have enough money")
        else:
            self.balance -= amount
            print(f"Please collect your amount {amount}")
            print(f"Remaining balance: {self.balance}")

    def details(self):
        print(f"Your name is {self.name}")
        print(f"Your account number is {self.acc_num}")
        print(f"Your balance is {self.balance}")
        print("Thanks for coming")


card = input("Enter your card new/old: ")
if card == "new":
    name = input("Enter your name: ")
    Account_num = int(input("Enter your account number: "))
    print("Going to pin generation section")
    enter = 4
    user01 = ATM(enter, name, Account_num)
else:
    user01 = ATM()
