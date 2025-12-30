# write a python program that take continuous input from user dynamically and store it in a file.

try:
    with open("text02.data","a") as fp:
        while True:
            data=input()
            if data != "stop":
                fp.write(data)
            else:
                print("All data are store into the text02 file")
                fp.close()
                break

except :
    print("check the logic first")