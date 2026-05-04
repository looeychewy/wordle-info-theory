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
Began working on implementing letter validity mechanicss

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

1.3
- Implement csv file to hold guess pool data (alts -> ?0)
"""

import random
import csv # use csv file instead of .py

# TODO: Type hints, docstrings, guess pool to a csv file
    # Function to find more common English words from the guess pool to only choose those as the answer?
    # Next: Double letter color priority mechanic (abase, terror, terry, etc.)
        # GUI -> tkinter app implementation next?
""" 
ie cluck (two c's)
Look for if letter count greater than 1? -> str.count()
player_guess initialize to a set?
    - pop letters from once detected to prevent double detection
    - list maybe?
"""

# ANSI Escape Codes for terminal coloring
# Terminal colors for guess scenarios (Background Color + Text Color concatenation)
GREEN  = "\033[42m" + "\033[30m"
YELLOW = "\033[43m" + "\033[30m"
GREY = "\033[100m"

# Clear terminal colors
CLEAR_COL = "\033[0m"


def get_input(prompt: str) -> str:
    """Helper function to get and keep player input at lowercase when they enter their Wordle guesses.

    Args:
        prompt (str): Prompts player to enter their guess, shows chances used and letter match output
    Returns:
        Prompt nested inside input function, set to lowercase

    """
    return input(prompt).lower()


def find_match(player_guess: str, word_answer: str) -> str:
    """Finds matching letters between player_guess and word_answer using zip() and set() -> groups into tuples, find length of set of tuples
    to determine if letters in these tuples are matches or not. Highlights letters GREEN, YELLOW, and GRAY accordingly.

    Args:
        player_guess (str): Player's guessed word
        word_answer (str): Actual answer determined by random.choice()
    Returns:
        Colorized output, individual letters colored in GREEN, YELLOW, and GRAY depending on if matches exist or not.

    """
    matches = ""

    for letters in zip(player_guess, word_answer):
        if letters[0] in word_answer and len(set(letters)) == 1:
            matches += f" {GREEN}{letters[0]}{CLEAR_COL}"  # Green  -> in word, correct place
        elif letters[0] in word_answer and len(set(letters)) != 1:
            matches += f" {YELLOW}{letters[0]}{CLEAR_COL}"  # Yellow -> in word, wrong place
        elif letters[0] not in word_answer:
            matches += f" {GREY}{letters[0]}{CLEAR_COL}"  # Gray -> not in word

    return matches

if __name__ == "__main__":
    player_guess = ""
    with open ("wordle-guess-pool.csv", newline='') as wordfile:
        reader = csv.reader(wordfile)
        data = [row[0] for row in reader]
        word_answer = random.choice(data)

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
                print(f"Correct! Word is {GREEN}{word_answer.upper()}{CLEAR_COL}!")
                break

        if chance_counter >= 6:
            print(f"\nSorry, the word was {GREY}{word_answer.upper()}{CLEAR_COL}")
