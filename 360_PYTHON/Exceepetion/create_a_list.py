my_list=[]
length=0
i=1

def add(element):
    global my_list
    my_list+=[element]

def length():
    global length
    try:
       len=int(input("length: "))
       length=len
    except:
        print("length must be integer")
        length()
    else:
        make_list()


def make_list():
    global length
    global i
    try:
        while length!=0:
            add(int(input(f"element {i}: ")))
            length-=1
            i+=1
    except:
        print("Enter  number  as element")
        make_list()
    else:
        print(my_list)
    
length()

