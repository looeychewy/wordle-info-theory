# unused ent. imports CURRENTLY
import numpy as np
from scipy import stats
from scipy.stats import entropy

import math
import random
import csv
from typing import List, Optional, Tuple
from collections import Counter

# ANSI codes
GREEN = "\033[42m" + "\033[30m"
YELLOW = "\033[43m" + "\033[30m"
GRAY = "\033[100m"
CLEAR_COL = "\033[0m"

CORRECT, PRESENT, ABSENT = 2, 1, 0  # dict keys determining green/yellow/grey respectively

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
        """Takes two input strings, checks which letters in guess match or exist the letters in answer.
        Returning a tuple consisting of the following defined validity keys (2 = CORRECT, 1 = PRESENT,
        0 = ABSENT) ordered by letter placement in guess.

        Args:
            guess (string): First input string that's being evaluated
            answer (string): Second input string that guess is being checked against

        Returns:
             tuple: Tuple that holds validity keys in order of appearance in guess"""
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

        return tuple(matches)

    def guess(self, guess: str) -> Matches:
        error = self.is_valid_guess(guess)
        if error:
            raise ValueError(error)
        self.attempts.append(guess)
        return self.find_match(guess, self.answer)

# Print visual letter color validity Wordle-style
def render_pattern(guess: str, pattern: Matches) -> str:
    color = {CORRECT: GREEN, PRESENT: YELLOW, ABSENT: GRAY}
    return "".join(f" {color[p]}{ch}{CLEAR_COL}" for ch, p in zip(guess, pattern))

# Normalizing input to lowercase letters
def get_input(prompt: str) -> str:
    return input(prompt).lower()

def calc_entropy(guess, word_pool) -> float:
    # shannon entropy: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.entropy.html
    # h(X) = "sigma/sum" over i of probability of outcome x_i occurring * the log of probabilities of ALL possible outcomes
    # H = -sum(pk * log(pk)) if only probabilities pk are given
    # PK IS ARRAY-LIKE

    word_entropy = 0
    pattern = WordleGame.find_match(guess, word_pool)
    return word_entropy

def wordle_game():
    guess_pool = WordleGame.load_word_list("guess_pool.csv")
    game = WordleGame(guess_pool)

    print(game.answer) # DELETE WHEN DONE -- for debugging
    # MAIN GAME LOOP
    while not game.is_over:
        guess = get_input(f"Chances used: {game.chances_used}. Enter your guess: ")

        # Validation check loop during game state
        error = game.is_valid_guess(guess)
        while error:
            guess = get_input(f"{error}: ")
            error = game.is_valid_guess(guess)
        pattern = game.guess(guess)

        # Creates new temporary pool for storing all possible words based on pattern equality
        temp_pool = [word for word in guess_pool if WordleGame.find_match(guess, word) == pattern]
        print(temp_pool, len(temp_pool))

        pattern_count = Counter()
        for word in temp_pool:
            asd = WordleGame.find_match(guess, word)
            pattern_count[asd] += 1
        print(pattern_count)
        # print(dict(pattern_count))  # Tracks num of each key in each tuple


        print(render_pattern(guess, pattern))


        # determine the entropic value of each guess
    if game.is_won:
        print(f"Correct! Word is {GREEN}{game.answer.upper()}{CLEAR_COL}!")
    else:
        print(f"\nSorry, the word was {GRAY}{game.answer.upper()}{CLEAR_COL}")


if __name__ == '__main__':
    wordle_game()