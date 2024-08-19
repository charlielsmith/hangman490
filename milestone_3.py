import random

words = ["apple", "banana", "cherry", "mango", "blueberry"]

random_word = random.choice(words)

print(words)

print("Randomly selected word:", random_word)

guess = ""

while True:
    guess = input("Please guess a letter: ")

    if len(guess) == 1 and guess.isalpha():
       break

    else:
        print("Invalid letter. Please enter a single alphabetical 
character.")

print("You guess:", guess)
