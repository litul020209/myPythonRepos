def subset(word):
    list_01=[]
    if len(word)==1:
        return word[0]
    list_01=word[0]+subset(word[1:])
    return list_01


print(subset("abc"))