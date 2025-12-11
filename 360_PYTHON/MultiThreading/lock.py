import threading

b=100

lock=threading.Lock()
def withdrw():
    global b
    for i in range(100):
        lock.acquire()
        b-=1
        lock.release()
thread=[]
for i in range(2):
    t=threading.Thread(target=withdrw)
    t.start()
    thread.append(t)

for t in thread:
    t.join()

print(f"balance:{b} ")

