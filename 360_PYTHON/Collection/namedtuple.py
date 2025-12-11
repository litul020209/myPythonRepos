from collections import namedtuple

nt=namedtuple("mytuple",("a","b","c","d","e"))

t1=nt(10,20,30,40,50)
print(t1)
