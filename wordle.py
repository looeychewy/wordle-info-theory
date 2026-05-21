import random
import csv

# ANSI Escape Codes for terminal colors -> guess scenarios (Background Color + Text Color concatenation)
GREEN  = "\033[42m" + "\033[30m"
YELLOW = "\033[43m" + "\033[30m"
GRAY = "\033[100m"

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


def find_match(play_guess: str, final_answer: str) -> str:
    """Finds matching letters between player_guess and word_answer using two-pass system:

    First pass looks for "GREEN" letters (in both words and in same place).
    Second pass looks for "YELLOW" (in both words but not same place) + "GRAY" letters (doesn't exist in answer)

    Instantiates a matches output list to hold colorized letters and an answer_letters pool to remove letters from if
    matches are found. Letters are highlighted GREEN, YELLOW, or GRAY accordingly based on match conditions.
    Args:
        play_guess (str): Player's guess word
        final_answer (str): Actual answer word
    Returns:
        Colorized string output, letters colored GREEN, YELLOW, GRAY depending on if matches were found
    """

    matches = [""] * len(final_answer) # Output list to hold colorized letters, length of word_answer (5)
    answer_letters = list(final_answer) # Instantiate an answer pool to "pop" letters from once found in both words

    # Two passes, first pass to look for green letters and consume from answer_letters
    for idx, (guess_letter, answer_letter) in enumerate(zip(play_guess, final_answer)):
        if guess_letter == answer_letter:
            matches[idx] = f" {GREEN}{guess_letter}{CLEAR_COL}"
            answer_letters[idx] = None # Set to None instead of .pop() to preserve list length

    # Second pass to look for yellow and gray letters (in answer but not same place, not in answer)
    for idx, guess_letter in enumerate(play_guess):
        if matches[idx]:
            continue # if green already, skip
        if guess_letter in answer_letters: # yellow letter condition
            matches[idx] = f" {YELLOW}{guess_letter}{CLEAR_COL}"
            answer_letters[answer_letters.index(guess_letter)] = None # "consume" found letter to prevent invalid double yellow
        else: # gray letter condition
            matches[idx] = f" {GRAY}{guess_letter}{CLEAR_COL}"

    return "".join(matches)

def wordle_game():
    pass

if __name__ == "__main__":

    player_guess = ""
    with (open("guess_pool.csv", newline='') as word_file):
        reader = csv.reader(word_file)
        data = [row[0] for row in reader]
        word_answer = random.choice(data)

    # Main gameplay loop, tracks chances used
    chance_counter = 0
    while chance_counter < 6:
        player_guess = get_input(f"Chances used: {chance_counter}. Output:{find_match(player_guess, word_answer)}. Enter your guess: ")

        # Continuously asks player to input valid guess if their input is not in the guess pool
        while player_guess != word_answer and player_guess not in data:
            if len(player_guess) != 5:
                player_guess = get_input("Guess should only be 5 characters, try again: ")
            else:
                player_guess = get_input("Word not in list, try again: ")

        # Player guess validity, determines whether guess is the correct answer
        if player_guess != word_answer and player_guess in data:
            chance_counter += 1
        elif player_guess == word_answer:
            print(f"Correct! Word is {GREEN}{word_answer.upper()}{CLEAR_COL}!")
            break

    if chance_counter >= 6:
        print(f"\nSorry, the word was {GRAY}{word_answer.upper()}{CLEAR_COL}")
