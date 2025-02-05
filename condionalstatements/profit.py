sell_price=int(input("enter the sell price:"))
cost_price=int(input("enter the cost price:"))
# profit=sell_price-cost_price
# if profit>0:
#     print("the seller made profit:",profit)
# if profit==0:
#     print("the seller made no profit and no loss")
    
# else:   
#     print("the seller made loss")
if sell_price>cost_price:
    print("the seller made profit ")
if sell_price<cost_price:
    print("the seller made loss ")
if sell_price==cost_price:
     print("the seller made no profit and no loss ")