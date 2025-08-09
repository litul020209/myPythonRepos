class bank:
    def __init__(self,owner,balance):
        
        self.owner_name=owner
        self.balance=balance
    def check_balance(self):
        print(f"Mr {self.owner_name} your total avaiable balance is {self.balance}")
    def withdraw(self):
        if self.balance==0:
            print(f"Mr {self.owner_name} your balance is 0 you can't withdraw money from your account")
            return
        else:
            self.want_money=int(input("enter your withdraw money: "))
            if self.want_money>self.balance:
                print(f"Mr {self.owner_name} your account have insufficent balance: ")
            else:
                print(f"Mr {self.owner_name} please collect your cash {self.want_money} ")
                print(f"Mr {self.owner_name} your total balance is now {self.balance-self.want_money}")

    def deposite(self):
        self.depo_money=int(input("enter your deposite  money: "))
        print(f"your total balance is now {self.balance+self.depo_money}")

user_01=bank("Litul Biswal",10000)
user_01.check_balance()
user_01.withdraw()
user_01.check_balance()
        