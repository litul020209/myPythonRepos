f1=open("file_01","r+")
f1.write("Hello World")
f1.seek(0)
print(f1.read())
f1.close()

f2=open("file_01","r")
d=f2.read()
print(d)
f2.close()

f3=open("file_01","w+")
p1=f3.read()
print(p1)
f3.write("motivation is nothing without your attention")
p2=f3.read()
print(p2)
f3.close()
# try:
#     with open("file_01", "x") as f:
#         f.write("Hello World")
# except FileExistsError:
#     print("File already exists!")

# with open("file_01", "r") as f:
#     print(f.read())
