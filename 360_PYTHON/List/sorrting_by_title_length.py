books=["AI", "Python Basics", "ML Systems", "Data"]

ans=[]

while True:
    max=""
    for x in books:
        if len(x)>=len(max):
            max=x
    ans.append(max)
    books.remove(max)
    if len(books)==0:
        break
print(ans)



