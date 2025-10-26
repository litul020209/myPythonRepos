words=["abcd","efkl","bklld","alt"]

ans=[]

for i in range(len(words)):
    for j in range(i+1,len(words)):
        if len(set(words[i]) & set(words[j])) >1:
            ans.append((words[i],words[j]))

print(ans) 