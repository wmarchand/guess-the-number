#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random


def get_number():
    return random.randint(1,100)

def difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        return 10
    elif difficulty == "hard":
        return 5
    else:
        print("You did not listen. You get one attempt to GUESS THE NUMBER!")
        return 1

def outcome(status):
    if status == "win":
        print(f"You have guessed the number whith {attempts} attempts remaining! Congrats, YOU WIN!!!")
    elif status == "lost":
        print(f"You have failed to guess the number. The correct number was {number}. Better luck next time!")

def play(player_guess, random_num):
    if player_guess == random_num:
        outcome("win")
        return 0
    elif player_guess > random_num:
        if attempts != 1:
            print("Too high.\nGuess again.")
        else:
            print("Too high for the last time!")
            outcome("lost")
        return attempts - 1
    elif player_guess < random_num:
        if attempts != 1:
            print("Too low.\nGuess again.")
        else:
            outcome("lost")
        return attempts - 1

keep_playing = True
while keep_playing:
    number = get_number()
    print(logo)
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    print(f"CHEAT CODE: {number}")
    attempts = difficulty()
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        score = play(guess, number)
        attempts = score
    wrong_answer = True
    while wrong_answer:
        answer = input("Would you like to play again? Type 'yes' or 'no': ").lower()
        if answer == 'yes':
            wrong_answer = False
        elif answer == 'no':
            print("Goodbye.")
            keep_playing = False
            wrong_answer = False
        else:
            print("Do you understand the words that are coming out of my mouth???")
            
        