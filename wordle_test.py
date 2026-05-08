import random
import csv # efficiency?

# TODO: Double letter color priority mechanic (abase, terror, terry, etc.)
    # Function to find more common English words from the guess pool to only choose those as the answer?
    # GUI/tkinter app implementation next for visualization?

""" 
ie cluck (two c's)
Look for if letter count greater than 1? -> str.count()
"""

# ANSI Escape Codes for terminal colors -> guess scenarios (Background Color + Text Color concatenation)
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

    # implement double letter here?
    # how does it work?
        # take player_guess and word_answer
        # compare individual letters between each one, see if there's matches
            # how account for letter frequency?
        # If letter is guessed more time than appears in answer, extra instances of said letter will show as
        # gray, even if it's in the answer otherwise

    matches = ""

    for i, (g, a) in enumerate(zip(player_guess, word_answer)):
        print(i, g, a)

    for letters in zip(player_guess, word_answer): # For each tuple in the zip object

        if letters[0] in word_answer and len(set(letters)) == 1:
            matches += f" {GREEN}{letters[0]}{CLEAR_COL}"  # Green  -> in word, correct place
        elif letters[0] in word_answer and len(set(letters)) != 1:
            matches += f" {YELLOW}{letters[0]}{CLEAR_COL}"  # Yellow -> in word, wrong place
        elif letters[0] not in word_answer:
            matches += f" {GREY}{letters[0]}{CLEAR_COL}"  # Gray -> not in word

    return matches

if __name__ == "__main__":
    player_guess = ""

    with open ("test_pool.csv", newline='') as wordfile:
        reader = csv.reader(wordfile)
        data = [row[0] for row in reader]
        word_answer = random.choice(data)

        print(word_answer) # Prints correct game answer for testing

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
            print(f"\nSorry, the word was {GREY}{word_answer.upper()}{CLEAR_COL}")
