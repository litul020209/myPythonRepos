def reverse(list_word):
    list_word.sort()
    ans_in="-".join(list_word)
    return ans_in

word="green-red-yellow-black-white"
list_word=word.split("-")
ans=reverse(list_word)
print(ans)