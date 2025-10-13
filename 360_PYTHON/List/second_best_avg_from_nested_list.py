scores = [
[78, 82, 91], 
[65, 68, 70], 
[88, 84, 89], 
[90, 91, 92] 
]
avg_score=[]
for  x in scores:
    avg=sum(x)/3
    avg_score.append(avg)
print(avg_score)

max1=avg_score[0]
max2=avg_score[1]
if max2>max1:
    max1,max2=max2,max1

for y in avg_score:
    if y>max1:
        max2=max1
        max1=y

print(max2)

     