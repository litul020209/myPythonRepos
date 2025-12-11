from threading import Thread,current_thread,active_count
import time 
start=time.perf_counter()
print(f"running state thread at first {active_count()}")
def thread01():
    
    for i in range(1,3):
        print("Thread -01")
        time.sleep(3)
    print("*"*10)


def thread02():
    
    for i in range(1,3):
        print("Thread -02")
        time.sleep(3)
    print("-"*10)



t1=Thread(target=thread01,daemon=True)
t2=Thread(target=thread02)

t1.start()
t2.start()

print(f"running state thread till now {active_count()}")
t1.join()
t2.join()


print("this is the main thread")
end=time.perf_counter()
print(f"running state thread at last {active_count()}")
print(f"{end-start}")
print(f"running state thread at last {active_count()}")