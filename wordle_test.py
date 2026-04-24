"""
1.0
Basic word guessing game with some core Wordle logic:
    - 6 chances to guess a 5-letter word, answer (singular) chosen from valid guess pool (50 random words for this case)
    - Player_guess check logic:
        - if guess is NOT answer AND in guess_pool, increment chance counter
            - if guess is NOT answer AND NOT in guess_pool -> "invalid, try again: "
            - if len(guess) > 5 characters -> "guess should only be 5 characters, try again: "
        - if guess is answer -> print answer, end game
        - if all chances used -> end game, print correct answer

1.01
Began working on implementing letter validity mechanics

1.1
Implemented letter match/mismatch mechanics:
    - find_match(): looks for matching letters between guess and answer using zip() and set() -> groups into tuples, find length of set of tuples
    - find_mismatch(): same logic as find_match, if length of set is greater than 1, mismatch

1.11
Added inserting blanks in find_match() if mismatches are found

1.2
- Implemented color denotation (Green, Yellow, Grey) for letter matching in find_match()
- Reworked/revised find_match()
- Expanded guess pool drastically for better gameplay -> set in an external file wordle_guess_pool.py
"""
import random
from wordle_guess_pool import guess_pool

# TODO: Double letter color denotation mechanic

"""
1. cluck (two c's)
"""

# ANSI Escape Codes for terminal coloring
# Terminal colors for guess scenarios (Background Color + Text Color concatentation)
GREEN  = "\033[42m" + "\033[30m"
YELLOW = "\033[43m" + "\033[30m"
GREY = "\033[100m"

# Clear terminal colors
CLEAR_COL = "\033[0m"

# Helper function to get and keep user input at lowercase
def get_input(prompt):
    return input(prompt).lower()

# Finds letter matches between player_guess and word_answer, highlights letters GREEN, YELLOW, GREY accordingly
def find_match(player_guess, word_answer):
    matches = ""

    # Looks for common letters in guess_pool + player_guess, sticks them into matches or mismatches variable
    for letters in zip(player_guess, word_answer): # For each tuple of zipped letters between player_guess and word_answer
        if letters[0] in word_answer and len(set(letters)) == 1: # If guess letter in answer and same place
            matches += f" {GREEN}{letters[0]}{CLEAR_COL}" # Highlight green
        elif letters[0] in word_answer and len(set(letters)) != 1: # If guess letter in answer but not same place
            matches += f" {YELLOW}{letters[0]}{CLEAR_COL}" # Highlight yellow
        elif letters[0] not in word_answer: # If guess letter not in answer
            matches += f" {GREY}{letters[0]}{CLEAR_COL}"

    return matches

player_guess = ""
word_answer = random.choice(guess_pool)
print(word_answer) # Prints correct game answer for testing

# Main gameplay loop, tracks chances used
chance_counter = 0
while chance_counter < 6:
    player_guess = get_input(f"Chances used: {chance_counter}. Output:{find_match(player_guess, word_answer)}. Enter your guess: ")

    # Continuously asks player to input valid guess if their input is not in the guess pool
    while player_guess != word_answer and player_guess not in guess_pool:
        if len(player_guess) != 5:
            player_guess = get_input("Guess should only be 5 characters, try again: ")
        else:
            player_guess = get_input("Word not in list, try again: ")

    # Player guess validity, determines whether guess is the correct answer
    if player_guess != word_answer and player_guess in guess_pool:
        chance_counter += 1
    elif player_guess == word_answer:
        print(f"Correct! Word is {word_answer.upper()}!")
        break

if chance_counter >= 6:
    print(f"\nSorry, the word was {word_answer.upper()}")


