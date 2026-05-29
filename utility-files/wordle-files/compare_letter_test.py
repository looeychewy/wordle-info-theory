"""
Recall that * unpacks an iterable and passes each individual element as an argument
zip() joins each letter by index -> flower, flow -> (f, f), (l, l), (o, o), etc.

words = ["flower", "flow", "flight"]
*words = flower flow flight
zip(*words) = (f, f, f), (l, l, l), etc.
"""

"""
Check if letter exists in the word
      -> yes? check if it's in the same place as the answer (zip() function)
          -> yes? green || no? yellow
      -> no? grey
"""

"""
 for letter in player_guess:
        if letter in word_answer:
            for letters in zip(player_guess, word_answer):
                if len(set(letters)) == 1:
                    HIGHLIGHT BG_GREEN
                else:
                    HIGHLIGHT BG_YELLOW
        else:
            HIGHLIGHT BG_GREY"""
import random

guess_pool = [
    "blind", "grind"]
word_answer = random.choice(guess_pool)
print(word_answer)
player_guess = input("Enter your guess: ")

# compare_letter would get called in middle of rest of program, within main game loop
# separate into determine match + mismatch functions?
def compare_letter(player_guess, word_answer):
    matches = ""
    mismatches = ""

    # Store zip object with inputs
    zipped_letters = zip(player_guess, word_answer)

    # Take zipped iterables of player_guess + word answer and put inside a list of tuples
    compare_list = list(zipped_letters)

    # Looks for common letters in guess_pool + player_guess, sticks them into matches or mismatches variable
    for letters in zip(player_guess, word_answer):
        if len(set(letters)) == 1:
            matches += letters[0]
        else:
            mismatches += letters[0]


    return compare_list, matches, mismatches

    prefix = ""
    # for letters in zip(player_guess, word_answer):
    #     if len(set(letters)) == 1:
    #         prefix += letters[0]


# OLD FIND_MISMATCH METHOD
# Finds letter mismatches between player_guess and word_answer, returns mismatched as a string
def find_mismatch(player_guess, word_answer):
    mismatches = ""

    # Looks for common letters in guess_pool + player_guess, sticks them into matches or mismatches variable
    for letters in zip(player_guess, word_answer):
        if len(set(letters)) > 1:
            mismatches += letters[0]

    return mismatches

if __name__ == "__main__":
    print(compare_letter(player_guess, word_answer))


