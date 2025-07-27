
try:
    num=int(input("enter the nemorator: "))
    dnum=int(input("enter the denomenetor: "))
    div_value=num/dnum
    print(div_value)

except ZeroDivisionError as e:
    print("ths is zero division error")
# except ValueError as e:
#     print("this is value error")
except TypeError as e :
    print("this is type error")
else:
    print("also in the code else section ")
finally:
    print("code in final section now")

print("now in out side ")