print("Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
# Generate a random number between 1 and 100
import random

number = random.randint(1, 100)
# Ask the user to guess the number
level = input("Choose a difficulty. Type 'easy' or 'hard': ")
guess = int(input("What's your guess? "))
if level == "easy":
  attempts = 10
else:
  attempts = 5
# Keep track of the number of guesses
while attempts > 0:
  if guess == number:
    print("You got it!")
    break
  elif guess > number:
    print("Too high.")
    attempts -= 1
    print(f"You have {attempts} attempts remaining.")
    guess = int(input("What's your guess? "))
  else:
    print("Too low.")
    attempts -= 1
    print(f"You have {attempts} attempts remaining.")
    guess = int(input("What's your guess? "))

if attempts == 0:
  print("You lost! The number was {number}.")
