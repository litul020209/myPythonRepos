from operator import ifloordiv
from selectors import SelectSelector

l01= [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_01=list(filter(lambda x: x%2==0 ,l01))
print(list_01)

list_02=list(map(lambda x:"even" if x%2==0 else x ,l01))
