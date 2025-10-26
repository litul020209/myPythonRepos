paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]

journy=[]

journy.append(paths[0][0])
journy.append(paths[0][1])

for i in range(len(paths)-1):
    k=journy[len(journy)-1]
    for x in paths:
        if x[0]==k:
            journy.append(x[1])
            break
    
print(f"journy from {journy[0]}  to {journy[len(journy)-1]} " )
    

