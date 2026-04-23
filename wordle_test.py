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

1.02
Implemented letter match/mismatch mechanics:
    - find_match(): looks for matching letters between guess and answer using zip() and set() -> groups into tuples, find length of set of tuples
    - find_mismatch(): same logic as find_match, if length of set is greater than 1, mismatch

1.03
Added inserting blanks in find_match() if mismatches are found
"""
import random

# ANSI Escape Codes for terminal coloring
# Letter highlight colors
BG_GREEN  = "\033[42m"
BG_YELLOW = "\033[43m"
BG_GREY = "\033[100m"

# Text colors
FG_BLACK = "\033[30m"
FG_WHITE = "\033[97m"

# Clear terminal colors
RESET = "\033[0m"


# Helper function to get and keep user input at lowercase
def get_input(prompt):
    return input(prompt).lower()

def find_match(player_guess, word_answer):
    matches = ""

    # Looks for common letters in guess_pool + player_guess, sticks them into matches or mismatches variable
    for letters in zip(player_guess, word_answer):
        if len(set(letters)) == 1:
            matches += letters[0]
        else:
            matches += "_"

    return matches

def find_mismatch(player_guess, word_answer):
    mismatches = ""

    # Looks for common letters in guess_pool + player_guess, sticks them into matches or mismatches variable
    for letters in zip(player_guess, word_answer):
        if len(set(letters)) > 1:
            mismatches += letters[0]

    return mismatches

# Rudimentary guess pool (will be expanded much larger later on)
guess_pool = [
"abide", "bland", "blank", "bleed", "blend", "blimp", "blink", "brain", "brawn", "breed", "brink", "bring", "brown",
    "chunk", "clamp", "cling", "cluck", "clump", "clunk", "crack", "cramp", "crane", "crate", "creed", "crimp", "drain",
    "drawn", "drink", "faker", "field", "fiend", "flame", "flake", "flare", "fling", "franc", "frank", "frame", "frown",
    "glare", "grail", "grain", "greed", "green", "laser", "later", "learn", "least", "maker", "maser", "plank"
]
# answer_pool = []

# TODO: Color denotation mechanics, answer pool from guess pool?
''' 
Color denotation:
    # Check which letters are:
        # in answer, right place
        # in answer, wrong place
        # not in answer
    # Add color highlights to terminal after
    
Use ANSI Escape codes -> link an external file?
'''

player_guess = ""

word_answer = random.choice(guess_pool)
# print(word_answer) # Prints correct game answer for testing

# Main gameplay loop, tracks chances used
chance_counter = 0
while chance_counter < 6:
    player_guess = get_input(f"Chances used: {chance_counter}. Letters matched: {find_match(player_guess, word_answer)}."
                             f" Letters mismatched: {find_mismatch(player_guess, word_answer)} Enter your guess: ")

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


