from collections import deque

dq=deque()
dq.append(10)
dq.appendleft(20)
dq.popleft()
print(list(dq))

dq=deque(maxlen=5)
dq.append(10)
dq.append(20)
dq.append(30)
dq.append(40)
dq.append(50)

print(list(dq))
dq.append(100)
print(list(dq))


dq=deque([1,2,3,4,5,6,7])
print(dq,type(dq))

dq.rotate(1)     #right rotate
print(list(dq))

dq.rotate(-1)    #left rotate
print(dq)

dq.extend([10,20,30])
dq.extendleft([50,60,70])
print(list(dq))



