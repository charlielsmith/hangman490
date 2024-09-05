import random

words = ["apple", "banana", "cherry", "mango", "blueberry"]

random_word = random.choice(words)

print(words)

print("Randomly selected word:", random_word)

guess = ""

def ask_for_input():
    while True:
        guess = input("Please guess a letter: ")
        if len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print("Invalid letter. Please enter a single alphabetical")

def check_guess(guess):
    guess = guess.lower()
    if guess in random_word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

while True:
    guess = ask_for_input()

    check_guess(guess)