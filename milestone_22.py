import random

# List of words
words = ["apple", "banana", "cherry", "mango", "blueberry"]

random_word = random.choice(words)

print(words)

print("Randomly selected word: ", random_word)

user_word = input("Please enter a word: ")

if len(user_word) == 1 and user_word.isalpha():
    print("Good guess!")

else:
    print("Oops! That is not a valid input.")