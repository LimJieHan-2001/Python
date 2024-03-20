import random

# List of words to choose from
words = ["apple", "banana", "orange", "grape", "pineapple", "strawberry", "watermelon", "peach", "kiwi", "blueberry"]

def choose_word(words):
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word

def hangman():
    word = choose_word(words)
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("Guess the word:")

    while attempts > 0:
        print(display_word(word, guessed_letters))
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print("Incorrect guess! Attempts left:", attempts)
            if attempts == 0:
                print("Sorry, you ran out of attempts! The word was:", word)
                break
        else:
            print("Correct guess!")

        if all(letter in guessed_letters for letter in word):
            print("Congratulations, you've guessed the word:", word)
            break

hangman()
