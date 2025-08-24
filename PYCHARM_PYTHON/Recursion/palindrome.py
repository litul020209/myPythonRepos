
def palindrome(n):
    if isinstance(n,int):
        n=str(n)

    if len(n)==1 or len(n)==0:
        return True

    if n[0]==n[len(n)-1]:
        ans=palindrome(n[1:len(n)-1])
    else:
        return False
    return ans
s="1221"
print(palindrome(s))
