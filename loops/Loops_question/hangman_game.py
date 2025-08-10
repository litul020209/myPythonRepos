# Simple Hangman Game

# Step 1: Choose a secret word
secret_word = "python"

# Step 2: Create a variable to store guessed letters
guessed_letters = []

# Step 3: Number of tries allowed
tries = 6

print("🎮 Welcome to Hangman Game!")
print("Guess the word, one letter at a time.")

# Step 4: Game loop
while tries > 0:
    # Display the current word with _ for missing letters
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word.strip())

    # Check if player has guessed all letters
    if all(letter in guessed_letters for letter in secret_word):
        print("🎉 Congratulations! You guessed the word:", secret_word)
        break

    # Ask for user's guess
    guess = input("Guess a letter: ").lower()

    # Check for valid input
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter only one alphabet letter.")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    # Add the guess to guessed_letters list
    guessed_letters.append(guess)

    # Check if guess is in the word
    if guess in secret_word:
        print("✅ Good guess!")
    else:
        tries -= 1
        print("❌ Wrong guess. Tries left:", tries)

# Step 5: Game over
if tries == 0:
    print("💀 Game over! The word was:", secret_word)
