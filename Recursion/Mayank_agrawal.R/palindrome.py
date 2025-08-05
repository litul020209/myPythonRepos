
def palindrome(str1):
    n=len(str1)
    if len(str1)==1 or len(str1)==0:
        return True
    if str1[0]!=str1[n-1]:
        return False
    return palindrome(str1[1:n-1])

str1="biswib"
print(palindrome(str1))