from os import lchmod
def upperLower(str1):
   uc=0
   lc=0
   for x in str1:
       if x.isupper():
           uc+=1
       elif x.islower():
           lc+=1
       else:
           pass
   return uc,lc

str_1="CampusX is an Online Mentorship Program fOr EnginEering studentS."
a=upperLower(str_1)
print(f"the total upper case letter is :{a[0]}")
print(f"the total upper case letter is :{a[1]}")

