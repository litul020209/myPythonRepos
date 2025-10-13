s1={range(1,10),1,}
s2 = set(range(1, 10 ))
s3=set()
s3.update(s2)
print(s3)
s4 ={y for x in s1 if type(x)==range for y in x}
print(s4)



