from itertools import chain

l1=[1,2]
l2=[3,4]

print(list(chain(l1,l2)))

#same also

print([*l1, *l2])