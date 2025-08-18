from collections import defaultdict
list_01=["a","b","a","c","d","u","f","d","a","b","g","j","h","f","u","k","p","g","l","p"]
freq = defaultdict(int)

for x in list_01:
        freq[x]+=1
    

print(freq)