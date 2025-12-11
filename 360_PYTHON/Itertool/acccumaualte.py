from itertools import accumulate

l1=[1,2,3,4,5]

print(list(accumulate(l1,lambda a,b: a*b))) #inhere we should 1st give the iterobject not in end.