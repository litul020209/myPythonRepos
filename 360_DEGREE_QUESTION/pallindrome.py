
def reverse_str(w):
    if not w:
        return ""
    return reverse_str(w[1:])+w[0]
w="naman"
rw=reverse_str(w)
if w==rw:
    print("the string is palindrome ")

else:
    print("the string is not a palindrome string")

