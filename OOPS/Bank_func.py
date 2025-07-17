class bank:
    def __init__(self):
        self.avl_blnc=0
        
    def deposite(self,Add_money):
        self.Add_money=Add_money
        self.avl_blnc=self.avl_blnc+self.Add_money
        return self.avl_blnc
    def WithDraw(self,draw_money):
        self.draw_money=draw_money
        if self.avl_blnc >= self.draw_money:
            self.avl_blnc=self.avl_blnc-self.draw_money
            return self.avl_blnc
        else:
            print("you can't wiwth draw ")
        

user_01=bank()
depo=int(input("enter the deposite amount: "))
total_balance=user_01.deposite(depo)
print(f" the net balance is {total_balance} ")
draw=int(input("enter the with_draw amount: "))
total_balance=user_01.WithDraw(draw)
print(total_balance)










        














