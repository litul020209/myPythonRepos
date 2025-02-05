n1=int(input("enter the n1 "))
n2=int(input("enter the n2"))
# value=int(input("enter the value"))

# match value:
#     case 1:
#          print(n1+n2)
#     case 2:
#           print(n1-n2)
#           value=int(input("enter the value"))
value=input()

match value:
    case "+":
         print(n1+n2)
    case "-":
          print(n1-n2)

