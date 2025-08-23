list_01=["a","b","a","c","d","u","f","d","a","b","g","j","h","f","u","k","p","g","l","p"]
dict={}
for x in list_01:
    if x in dict.keys():
        continue
       
    else:
        dict[x]=list_01.count(x)

print(dict)
print(len(dict))