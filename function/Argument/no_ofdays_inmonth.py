def days(year,month):
    m=month
    y=year
    calander=["january" ,"february" ,"march" ,"april" ,"may" ,"june" ,"jully" ,"august" ,"september" ,"october" ,"november" ,"december"]
    for i in range(1,m+1):
        for j in range (i):
            if i==month:
                if (year%4==0  and year%100!=0) or year%400==0:
                    if month>=1 and month<=7:
                        if month % 2==0:
                            if month ==2 :
                                print(f"the month  {calander[month-1]} is 29 days because of the leaep year")
                                break
                            else:
                                print(f"the month  {calander[month-1]} is 30 days ")
                                break
                        else:
                            print(f"the month {calander[month-1]} is 31 days")
                            break
                    elif month>=8 and month<=12:
                        if month % 2==0:
                            print(f"the month  {calander[month-1]} is 31 days ")
                            break
                        else:
                            print(f"the month {calander[month-1]} is 30 days")
                            break 
                else:
                    if month>=1 and month<=7:
                        if month % 2==0:
                            if month ==2 :
                                print(f"the month  {calander[month-1]} is 28 days ")
                                break
                            else:
                                print(f"the month  {calander[month-1]} is 30 days ")
                                break
                        else:
                            print(f"the month {calander[month-1]} is 31 days")
                            break
                    elif month>=8 and month<=12:
                        if month % 2==0:
                            print(f"the month  {calander[month-1]} is 31 days ")
                            break
                        else:
                            print(f"the month {calander[month-1]} is 30 days")
                            break
    return       

print(days(1233,2))