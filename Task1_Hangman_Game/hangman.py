import random

# List of predefined words
words = ["python", "apple", "computer", "network", "coding"]

# Select a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of incorrect guesses allowed
attempts = 6

print("===== HANGMAN GAME =====")

while attempts > 0:

    display_word = ""

    # Create the hidden word
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if the word is completely guessed
    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    # Check if only one letter is entered
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet.")
        continue

    # Prevent duplicate guesses
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct Guess!")
    else:
        attempts -= 1
        print("Wrong Guess!")
        print("Remaining Attempts:", attempts)

# If attempts become 0
if attempts == 0:
    print("\nGame Over!")
    print("The correct word was:", word)