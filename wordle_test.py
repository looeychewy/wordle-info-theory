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
"""
import random

# **Is an answer pool needed right now?**

guess_pool = [
"abide", "bland", "blank", "bleed", "blend", "blimp", "blink", "brain", "brawn", "breed", "brink", "bring", "brown",
    "chunk", "clamp", "cling", "cluck", "clump", "clunk", "crack", "cramp", "crane", "crate", "creed", "crimp", "drain",
    "drawn", "drink", "faker", "field", "fiend", "flame", "flake", "flare", "fling", "franc", "frank", "frame", "frown",
    "glare", "grail", "grain", "greed", "laser", "later", "learn", "least", "maker", "maser", "plank"
]
# answer_pool = []

# TODO: Color denotation mechanics, answer pool from guess pool?

# Color denotation:
    # Check which letters are:
        # in answer, right place
        # in answer, wrong place
        # not in answer
    # Add color highlights to terminal after

# Check if letters in player_guess are in the same index in word_answer
    # "python character comparison"
    # Nest into function?
        # compare_char = [word_answer, player_guess]
        # zip(*compare_char)
        # ---- Alternatively ----
        # compare_char(player_guess, word_answer)
    # would take returned function value and use to denote letter validity

word_answer = random.choice(guess_pool)
print(word_answer) # use for testing

chance_counter = 0
while chance_counter < 6:
    player_guess = input(f"Chances used: {chance_counter}. Enter your guess: ").lower()

    while player_guess != word_answer and player_guess not in guess_pool:
        if len(player_guess) > 5:
            player_guess = input("Guess should only be 5 characters, try again: ").lower()

        player_guess = input("Invalid, enter your guess: ").lower()

    if player_guess != word_answer and player_guess in guess_pool:
        chance_counter += 1
    elif player_guess == word_answer:
        print(f"Correct! Word is {word_answer}!")
        break

if chance_counter >= 6:
    print(f"\nSorry, the word was {word_answer}")


