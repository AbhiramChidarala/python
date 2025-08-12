#Python random guessing game 

import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num,highest_num)

guesses = 0
is_running = True

print("Python Number Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}.")

while is_running:

    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1 

        if guess < lowest_num or guess > highest_num:
            print("that number is out of range")
            print(f"PLZ Select a number between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("Your guess is too low")
        elif guess > answer:
            print("Your guess is too high")
        else : 
            print(f"correct! The answer was {answer}")
            print(f"number of guesses : {guesses}")
            is_running = False

    else:
        print("Invalid guess")
        print(f"PLZ Select a number between {lowest_num} and {highest_num}")
