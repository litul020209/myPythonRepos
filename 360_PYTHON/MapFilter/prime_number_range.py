start,end=int(input("start:")),int(input("end:"))
print(list(filter(lambda x:len(list(filter(lambda y:x%y==0,range(1,x+1))))==2,range(start,end+1))))

print(list(filter(lambda x:len([y for y in range(1,x+1) if x%y==0])==2,range(start,end+1))))