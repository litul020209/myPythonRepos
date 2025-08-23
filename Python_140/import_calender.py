import calendar
import datetime

year=int(input("enter the year: "))
month=int(input("enter the month: "))
cal=calendar.month(year,month)
print(cal)