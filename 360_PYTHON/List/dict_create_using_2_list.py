product_name=["Lays","Bingo","Dorito","Uncle Chip","Too Yumm"]

price=[5,5,10,20,25]

price_product={x:y  for x,y in zip(product_name,price)}

print(price_product)