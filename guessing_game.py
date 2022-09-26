"""
Project 1 - Number Guessing Game
--------------------------------

For this first project you can use Workspaces. 

NOTE: If you prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

from random import random
from statistics import median
from statistics import mode
from statistics import mean
import sys

guess_counts = [];

def get_new_guess(text):    
    try:
        return int(input(text))
    except (ValueError, TypeError):
        return get_new_guess("That is not a valid value.. Try again: ")
        

def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Save their attempt number to a list.
    6. At the end of the game, show the player, 1) their number of attempts, 2) the mean, median, and mode of the saved attempts list.
    7. Ask the player if they want to play again.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    
    
    SOLUTION = int(random() * 100)
    
    if len(guess_counts) != 0:
        high_score = min(guess_counts)
        print("##### Welcome back! #####")
        print(f"Can you beat the high score of {high_score} attempts?")
    else:
        print("##### Welcome to this Number Guessing Game #####")
    
    guess = get_new_guess("Guess a number between 1 and 100: ")
    attempts_count = 1;
        
    while guess != SOLUTION:
        
        if guess > 0 and guess <= 100:
            if guess > SOLUTION:
                print(f"It's lower. Try again")
            else:
                print(f"It's higher. Try again")
            
            attempts_count += 1
            guess = get_new_guess("Guess a number: ")
        else:
            guess = get_new_guess("Try guessing a number between 1 and 100: ")
    
    
    guess_counts.append(attempts_count)
    
    median_score = median(guess_counts)
    mode_score = mode(guess_counts)
    mean_score = mean(guess_counts)
                
    print("You got it! Nicely done! ")
    print(f"You only needed {attempts_count} attempts to make it right! ")
    print("### Here are some awesome stats for you ###")
    print(f"Median: {median_score}")
    print(f"Mode: {mode_score}")
    print(f"Mean: {mean_score}")
    
    start_over = input("Do you want to start over? Y/N   ").lower()
    
    if start_over == "y":
        start_game()
    else:
        sys.exit("Welcome back any time :)")
    

# Kick off the program by calling the start_game function.
start_game()