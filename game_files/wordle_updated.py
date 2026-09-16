# shannon entropy: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.entropy.html
# h(X) = "sigma/sum" over i of probability of outcome x_i occurring * the log of probabilities of ALL possible outcomes
    # H = -sum(pk * log(pk)) if only probabilities pk are given
    # PK IS ARRAY-LIKE

# 3^5 = 243 possible pattern outcomes
    # 3 possible outcomes (green, yellow, gray)
    # 5 letters per wordle guess

# 1. Establish candidate pool -> define list of all remaining valid answers not yet eliminated by past guesses ✅
    # a. From temp pool (start of game, that's the entire list)
    # Draw up a second list that only exists during game state/runtime(?), duped from guess_pool.csv ✅
    # to think about later: is a second list actually needed?
# With each valid answer that passes through, POP it at the index until game ends, which then ✅

# 2. Select candidate guess?

# dicts
    # 1. Return tuple accessed from returning find_match
    # 2. Enter new tuple matches (ie (1, 1, 1, 0, 0) into dict with each valid guess that passes through
    # 3. If tuple already exists within dict object increase the "value part of the key-value pair by 1"
    # 4. Collections.counter to determine the frequency of each pattern distribution?

# unused ent. imports CURRENTLY
import numpy as np
from scipy import stats
from scipy.stats import entropy

import random
import csv
from typing import List, Optional, Tuple

# ANSI codes
GREEN = "\033[42m" + "\033[30m"
YELLOW = "\033[43m" + "\033[30m"
GRAY = "\033[100m"
CLEAR_COL = "\033[0m"

CORRECT, PRESENT, ABSENT = 2, 1, 0  # dict keys, ez

# self note: nest usage value inside self-defined name
Matches = Tuple[int, ...] # Type aliasing, increased readability

class WordleGame:
    def __init__(
        self,
        guess_pool: List[str],
        answer_pool: Optional[List[str]] = None,
        answer: Optional[str] = None,
        rng: random.Random = random,
        max_attempts: int = 6,
    ):
        self.guess_pool = guess_pool
        self.answer_pool = answer_pool if answer_pool is not None else guess_pool
        self.answer = answer or rng.choice(self.answer_pool) # format allows for easier testing
        self.attempts: List[str] = []
        self.max_attempts = max_attempts

# Loads word pool
    @staticmethod
    def load_word_list(path: str) -> List[str]:
        with open(path, newline='') as word_file:
            reader = csv.reader(word_file)
            data = list(reader)
            return [row[0] for row in data]

            # return [row[0] for row in reader]

# Class properties
    @property
    def chances_used(self) -> int:
        return len(self.attempts)

    # Checks if the most recent player guess is the answer
    @property
    def is_won(self) -> bool:
        return bool(self.attempts) and self.attempts[-1] == self.answer

    @property
    def is_over(self) -> bool:
        return self.is_won or self.chances_used >= self.max_attempts

# --- guess validity ----
    def is_valid_guess(self, guess: str):
        if not guess.isalpha():
            return "Guess should only be letters, try again"
        if len(guess) !=  len(self.answer):
            return f"Guess should only be {len(self.answer)} characters, try again"
        if guess != self.answer and guess not in self.guess_pool:
            return "Word not in list, try again"

        return None

# --- find match ---
    @staticmethod
    def find_match(guess: str, answer: str) -> Matches:
        matches = [ABSENT] * len(answer)
        remaining = list(answer)

        for idx, (guess_letter, answer_letter) in enumerate(zip(guess, answer)):
            if guess_letter == answer_letter:
                matches[idx] = CORRECT
                remaining[idx] = None

        for idx, guess_letter in enumerate(guess):
            if matches[idx] == CORRECT:
                continue
            if guess_letter in remaining:
                matches[idx] = PRESENT
                remaining[remaining.index(guess_letter)] = None

        # make new tuple guess_pattern and return it OR global tuple object to be able to be accessed anywhere?
        # guess_pattern = tuple(matches)
        # return guess_pattern

        print(tuple(matches)) # visualization of dict keys tuple
        return tuple(matches)

    def guess(self, guess: str) -> Matches:
        error = self.is_valid_guess(guess)
        if error:
            raise ValueError(error)
        self.attempts.append(guess)
        return self.find_match(guess, self.answer)

# Print visualization of validity of each letter Wordle-style
def render_pattern(guess: str, pattern: Matches) -> str:
    color = {CORRECT: GREEN, PRESENT: YELLOW, ABSENT: GRAY}
    return "".join(f" {color[p]}{ch}{CLEAR_COL}" for ch, p in zip(guess, pattern))

# Normalizing input to lowercase letters
def get_input(prompt: str) -> str:
    return input(prompt).lower()


def wordle_game():
    guess_pool = WordleGame.load_word_list("guess_pool.csv")

    # Temp word pool strictly for data manipulation
    temp_pool = WordleGame.load_word_list("guess_pool.csv")

    game = WordleGame(guess_pool, temp_pool)

    print(game.answer)
    while not game.is_over:
        guess = get_input(f"Chances used: {game.chances_used}. Enter your guess: ")

        # Validation check loop during game state
        error = game.is_valid_guess(guess)
        while error:
            guess = get_input(f"{error}: ")
            error = game.is_valid_guess(guess)

        pattern = game.guess(guess) # Returns tuple Matches of the "correct" keys

        # -> find location of *guess* and pop it from the list
        # still need the number of remaining guesses from temp_pool
        x = temp_pool.pop(guess_pool.index(guess))
        n = len(temp_pool)

        print(x, x in temp_pool, x in guess_pool, len(temp_pool), len(guess_pool)) # not in temp, in guess ✅

        print(render_pattern(guess, pattern))

    if game.is_won:
        print(f"Correct! Word is {GREEN}{game.answer.upper()}{CLEAR_COL}!")
    else:
        print(f"\nSorry, the word was {GRAY}{game.answer.upper()}{CLEAR_COL}")

if __name__ == '__main__':
    wordle_game()