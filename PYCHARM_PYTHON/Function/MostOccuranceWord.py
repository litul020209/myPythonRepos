from collections import Counter

def mostOccuranceWord(dict01):
    m=0
    ans=""
    for k,v in dict01.items():
        if dict01[k]>=m:
            m=dict01[k]
            ans=k
    return f"{ans} --> {m}"



str_1="hello how are you i am fine thank you"
list_str1=str_1.split(" ")
count=Counter(list_str1)
print(mostOccuranceWord(count))