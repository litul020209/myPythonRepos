def halve_rev_str(word,len):
    if len==0:
        return word
    a=word[0]
    sans=halve_rev_str(word[1:],len-1)
    ans=sans+a
    return ans

str1=input("Enter your string: ")
length=0
for x in str1:
    length+=1
print(length)
if length%2==0:
    mid=length//2
else:
    mid=(length//2)+1

res=halve_rev_str(str1[mid:],mid-1)
print(str1[:mid]+res)
