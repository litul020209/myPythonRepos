list_01=["a","b","a","c","d","u","f","d","a","b","g","j","h","f","u","k","p","g","l","p"]
freq={}

for x in list_01:
    if x not in freq:
        freq[x]=1
    else:
        freq[x]=freq[x]+1

print(freq)