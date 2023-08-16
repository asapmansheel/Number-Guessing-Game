from art import logo
import random

EASY_TURNS = 10
HARD_TURNS = 5

def check_answer(guess, answer, turns):
    if guess > answer:
        print("Guess is too high")
        return turns - 1
    elif guess < answer:
        print("Guess is too low")
        return turns - 1
    else:
        print("Correct")

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    
    if level == "easy":
        return EASY_TURNS
    elif level == "hard":
        return HARD_TURNS
        

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
answer = random.randint(1, 100)
guess = 0

turns = set_difficulty()

while guess != answer and turns != 0:
  print(f"You have {turns} attempts remaining to guess the number.")
  guess = int(input("Make a guess: "))
  turns = check_answer(guess, answer, turns)

  if turns == 0:
      print("You have run out of guesses")
  elif guess != answer:
      print("Guess again")

print(f"The answer was {answer}")
    
          