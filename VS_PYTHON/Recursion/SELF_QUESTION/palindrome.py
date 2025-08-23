
def palindrome_func(str_1,ans):
    
    if not  str_1:
        return ans
    
    return palindrome_func(str_1[1:],str_1[0]+ans)
ans=""
str_1=input("enter the word: ")
print(palindrome_func(str_1,ans))
