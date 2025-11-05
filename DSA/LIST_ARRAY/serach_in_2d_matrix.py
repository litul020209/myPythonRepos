matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
n=count(matrix)
a=False
for i in range(n):
    if target in matrix[i]:
        a=True
        print( True )
        break
if not a:
    print( False )