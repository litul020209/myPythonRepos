salaries = [45000,52000,60000,48000]
ratings = [4.2,3.5,4.8,4.9]
ans=[]
for i in range(len(salaries)):
    if salaries[i]>50000 and ratings[i]>4:
        ans.append(salaries[i])

print(ans)