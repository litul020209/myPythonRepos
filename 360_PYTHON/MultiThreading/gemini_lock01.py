# import threading

# # 1. The Shared Data
# counter = 0

# def increment_without_lock():
#     global counter
    
#     # 2. The Critical Section
#     # In CPython, 'counter = counter + 1' is NOT a single step.
#     # It involves these 3 steps:
#     # A. Read: Read the current value of 'counter' (e.g., 5)
#     # B. Modify: Calculate the new value (5 + 1 = 6)
#     # C. Write: Write the new value back to 'counter' (e.g., counter becomes 6)
    
#     for _ in range(5000):
#         current_value = counter
#         new_value = current_value + 1
#         counter = new_value 

# # We run this function 5,000 times in two different threads.
# # Expected final value: 5000 + 5000 = 10000

# thread1 = threading.Thread(target=increment_without_lock)
# thread2 = threading.Thread(target=increment_without_lock)

# thread1.start()
# thread2.start()

# thread1.join()
# thread2.join()

# print(f"Final counter value: {counter}")




# import threading

# # 1. The Shared Data
# counter = 0
# # 2. Create the Lock object
# lock = threading.Lock() 

# def increment_with_lock():
#     global counter
    
#     for _ in range(5000):
#         # 3. ACQUIRE the Lock
#         with lock:
#             # This is now the PROTECTED critical section.
#             # No other thread can enter this 'with' block until the current one exits.
#             current_value = counter
#             new_value = current_value + 1
#             counter = new_value
#         # The lock is automatically RELEASED when the 'with' block ends.

# # ... The rest of the setup is the same ...
# thread1 = threading.Thread(target=increment_with_lock)
# thread2 = threading.Thread(target=increment_with_lock)

# thread1.start()
# thread2.start()

# thread1.join()
# thread2.join()

# print(f"Final counter value: {counter}") # Will now correctly print 10000