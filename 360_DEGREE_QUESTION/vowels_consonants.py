string_word=input("enter the word: ")
word=string_word.lower()
vowels=0
consonant=0
for i in word:
    if (i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
        vowels=vowels+1
    else:
      consonant=consonant+1

print(f"the number of vowels in {string_word} is {vowels} and the number of consonant in {string_word} is {consonant} ")