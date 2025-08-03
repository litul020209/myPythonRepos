str_01="A man, a plan, a canal: Panama"
str_02=""
for x in str_01:
    if x.isnum():
        str_02=str_02+x
    else:
        continue
str_02=str_02.lower()
str_03=str_02[::-1]

if str_02==str_03:
    print("the sentence is palindrome number ")
else:
    print("the sentence is not a palindrome")