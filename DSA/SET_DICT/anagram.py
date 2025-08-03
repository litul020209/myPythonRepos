s="anagram"
t="nagaran"
list_01=[]
list_02=[]
for x in s:
    list_01.append(x)
for y in t:
    list_02.append(y)

list_01.sort()
list_02.sort()
if list_01==list_02:
    print("anagram")
else:
    print("not anagram")

          
