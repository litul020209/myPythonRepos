from threading import Thread

import time

def thread01(start,end):
    print(start)
    print(end)

t1=Thread(target=thread01,args=(10,20))
t1.start()
t1.join()

