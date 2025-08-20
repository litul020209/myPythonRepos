# Simple Hangman Game
secret_word = "python"


guessed_letters = []


tries = 6

print("🎮 Welcome to Hangman Game!")
print("Guess the word, one letter at a time.")

while tries > 0:
    
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word.strip())

    
    if all(letter in guessed_letters for letter in secret_word):
        print("🎉 Congratulations! You guessed the word:", secret_word)
        break

    
    guess = input("Guess a letter: ").lower()

    
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter only one alphabet letter.")
        continue

    
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    
    guessed_letters.append(guess)

    
    if guess in secret_word:
        print("✅ Good guess!")
    else:
        tries -= 1
        print("❌ Wrong guess. Tries left:", tries)

if tries == 0:
    print("💀 Game over! The word was:", secret_word)
