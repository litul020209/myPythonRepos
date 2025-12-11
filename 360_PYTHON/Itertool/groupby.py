from itertools import groupby

l1=[1,2,3,4,5,6,2,3,1,5,6,7,1,2,3,5,6,7]

for k,g in groupby(sorted(l1)):
    print(k,"------>",len(list(g)))

l2=[(1,"dev"),(2,"test"),(3,"hr"),(4,"dev"),(5,"test"),(7,"hr")]

for k,g in groupby(sorted(l2,key=lambda x:x[1])):
    print(k,"------>",len(list(g)))

    
    