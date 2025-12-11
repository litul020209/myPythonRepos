from threading import Thread,current_thread,active_count
import time 
start=time.perf_counter()
print(f"running state thread at first {active_count()}")
def thread01():
    current_thread().name="CPU"  #ste the name of thread
    print(current_thread().name)  #to print current thread name
    for i in range(1,6):
        print("Thread -01")
    print("*"*10)


def thread02():
    current_thread().name="RAM"
    print(current_thread().name)
    for i in range(1,6):
        print("Thread -02")
    print("-"*10)

def thread03():
    current_thread().name="IO"
    print(current_thread().name)
    for i in range(1,6):
        print("Thread -02")
    print("#"*10)


t1=Thread(target=thread01)
t2=Thread(target=thread02)
t3=Thread(target=thread03)
t1.start()
t2.start()
t3.start()
print(f"running state thread till now {active_count()}")
t1.join()
t2.join()
t3.join()

print("this is the main thread")
end=time.perf_counter()
print(f"{end-start}")
print(f"running state thread at  {active_count()}")