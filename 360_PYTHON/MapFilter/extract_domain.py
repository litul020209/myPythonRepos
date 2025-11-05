mail=["yourname@gmail.com","yourname@outlook.com","yourname@icloud.com","yourname@yahoo.com"]

print(list(map(lambda x:x[x.index("@")+1:],mail)))