


def vowel(s):
    s=s.lower()
    vowels=["a","e","i","o","u"]
    ans=list(filter(lambda x:x not in vowels,s))
    ans=list(filter(lambda x: x not in " ",ans))
    res="".join(ans)
    return res

str_1="Virat the run machine kohli is the one and only modern bats man how achieved rank1 in all three format"
print(vowel(str_1))
