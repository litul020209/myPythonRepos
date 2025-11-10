from math_operation.geometry.circle import areaOfCircle,CircumferenceOFCircle
from math_operation.geometry.rectangle import areaOfRectangle,perimeterOfRectangle
from math_operation.geometry.square import areaOfSquare,perimeterOfSquare
from math_operation.geometry.rhombus import areaOfRhombus ,perimeterOfRhombus
from math_operation.geometry.triangle import areaOfTriangle,perimeterOfTriangle
from math_operation.geometry.trapezium import areaOfTrapezium,perimeterOfTrapeizium
from math_operation.geometry.parallelogram import areaOfParallelogram,perimeterOfParallelogram



print("1> for circle,2> for rectangle ,3> for square ,4> for rhombus ,5> for trangle ,6> for trapezium ,7> for parallelogram")
option=int(input("Enter your 2d shape number  from above option: "))

match option:
    case 1:
        r=int(input("Enter the radius of circle: "))
        res1=areaOfCircle(r)
        res2=CircumferenceOFCircle(r)
        print(f"area of circle is {res1} and circumference of circle is {res2}")

    case 2:
        l=int(input("Enter the length of rectangle: "))
        b=int(input("Enter the breadth of rectangle: "))
        res1=areaOfRectangle(l,b)
        res2=perimeterOfRectangle(l,b)
        print(f"area of rectangle is {res1} and perimeter of rectangle is {res2}")

    case 3:
        s=int(input("Enter the side of square: "))
        res1=areaOfSquare(s)
        res2=perimeterOfSquare(s)
        print(f"area of square is {res1} and perimeter of square is {res2}")
    case 4:
        b=int(input("Enter the base of rhombus: "))
        h=int(input("Enter the height of rhombus: "))
        res1=areaOfRhombus(b,h)
        res2=perimeterOfRhombus(b)
        print(f"area of rhombus is {res1} and perimeter of rhombus is {res2}")
    case 5:
        a=int(input("Enter side a: "))
        b=int(input("Enter side b: "))
        c=int(input("Enter side c: "))
        res1=areaOfTriangle(a,b,c)
        res2=perimeterOfTriangle(a,b,c)
        print(f"area of trangle is {res1} and perimeter of rhombus is {res2}")
        
    case 6:
        a=int(input("Enter side of parallel a: "))
        b=int(input("Enter side of parallel b: "))
        c=int(input("Enter side c: "))
        d=int(input("Enter side d: "))
        h=int(input("Enter the height h: "))
        res1=areaOfTrapezium(a,b,h)
        res2=perimeterOfTrapeizium(a,b,c,d)
        print(f"area of trapizium is {res1} and perimeter of trapizium is {res2}")
    case 7:
        b=int(input("Enter base b: "))
        h=int(input("Enter height h: "))
        s=int(input("Enter side s: "))
        res1=areaOfParallelogram(b,h)
        res2=perimeterOfParallelogram(b,s)
        print(f"area of parallelogram is {res1} and perimeter of parallelogram is {res2}")
    case _:
        print("Enter the above number for your shape")