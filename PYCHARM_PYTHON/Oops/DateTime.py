import datetime
from datetime import date, time, datetime, timedelta

class Product:
    def __init__(self):
        self.manufacturing_date=date.today()
        self.expiry_date= self.manufacturing_date + timedelta(days=2*365)

    def __str__(self):
        return f"manufacturing date is {self.manufacturing_date} and expiry date is {self.expiry_date}"
    def display(self):
        self.validity=self.expiry_date-self.manufacturing_date
        years = self.validity.days // 365
        months = (self.validity.days % 365) // 30
        days = (self.validity.days% 365) % 30
        return f"{years} years  {months} months {days} days are present for this product"

product1=Product()
print(product1)
print(product1.display())