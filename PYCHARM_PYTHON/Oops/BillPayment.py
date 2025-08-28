
class Bill:
    def due_clear(method):
        if method == "cheque":
            print("your cheque is processing....")
            print("your cheque is validity ")
            print("thanks for coming")
        elif method == "cash":
            print("we send our employee so please give the exact amount in our bill not give any extra rupees in here")
            print("thanks for coming")
        elif method=="online":
            print("please enter your billing id correctly ")
            print("please enter the exact amount")
            print("your payment is successfully debited ")
            print("thanks for coming")

class Payment(Bill):
    def payment_method(method):
        billing=Bill.due_clear(method)
        return billing
user1=Payment()
user1.payment_method("cheque")



