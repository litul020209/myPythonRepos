class BookNotFoundError(Exception):
    pass
class LimitExceedError(Exception):
    pass

class Book:
    def __init__(self,id,title,author,price,available_copies):
        self.id=id
        self.title=title
        self.author=author
        self.price=price
        self.available_copies=available_copies
        
class Student:
    def __init__(self,rollno):
        self.roll_no=rollno
        self.borrowed_book=[]

class Library:
    books=[]
    def add_book(self,id,title,author,price,available_price):
        b=Book(id,title,author,price,available_price)
        Library.books.append(b)

    

    def search_book(self,title,author):
        a=False
        for b in Library.books:
            if b.title==title and b.author==author:
                a=True
                return b
        if a==False:
            return False    


    def borrow_book(self, student, title, author):
        try:
            if len(student.borrowed_book) >= 3:
                raise LimitExceedError

            book = self.search_book(title, author)
            if not book:
                raise BookNotFoundError

            if book.available_copies == 0:
                raise BookNotFoundError

            student.borrowed_book.append(book)
            book.available_copies -= 1
            print("Book borrowed successfully")

        except BookNotFoundError:
            print("Book not found or unavailable")

        except LimitExceedError:
            print("You reached the maximum 3 book limit")    

s1=Student(1)
s2=Student(2)
s3=Student(3)

l1=Library()
l1.add_book(1001,"Physics","HC Verma",800,8)
l1.add_book(1002,"Chemistry","OP Tandon ",600,10)
l1.add_book(1003,"Math","RD Sharma",1200,0)
l1.borrow_book(s1,"Physics","HC Verma")

