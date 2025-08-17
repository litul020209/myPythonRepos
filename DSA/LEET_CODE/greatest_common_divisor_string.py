# str1 ="ABCAAABCAAABCAA"
# str2 ="ABCAAABCAAABCAA"
# print(str1+str2)
# if str1+str2 == str2+str1:
#     s1=len(str1)
#     s2=len(str2)
#     mn=min(s1,s2)
#     if mn==str1:
#         fstr=str1
#     else:
#         fstr=str2
    
#     compare=""
#     for x in fstr:
#         compare=compare+x
#         l=len(compare)
#         e=l+l
#         while e<=mn:
#             if compare==fstr[l:e]:
#                 l=e
#                 e=e+l
#             else:
#                 break
#         if l==mn:
#            break 
            
# print(compare)

str1 ="TAUXXTAUXXTAUXXTAUXXTAUXX"
str2 ="TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"

if str1+str2 == str2+str1:
    s1=len(str1)
    s2=len(str2)
    mn=min(s1,s2)
    if mn==len(str1):
        fstr=str1
    else:
        fstr=str2
    
    compare=""
    for x in fstr:
        compare=compare+x
        l=len(compare)
        add=l
        e=l+l
        while e<=mn:
            if compare==fstr[l:e]:
                
                l=e
                e=e+add
            else:
                break
        if l==mn:
           break 
            
print(compare)        
    

      
               





