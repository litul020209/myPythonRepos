n=int(input("Enter the number of books: "))
i=1
p=[]
while i<=n:
    a=int(input(f"Enter the number of pages of  books {i}: "))
    p.append(a)
    i+=1

print(p)
sm=sum(p)
l=len(p)

avg_page_read=sm//l
print(avg_page_read+1)

