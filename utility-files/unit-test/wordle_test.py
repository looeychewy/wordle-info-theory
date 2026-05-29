# Unittest for wordle.py

import unittest
from wordle import find_match, get_input, wordle_game

# Write GOOD tests, not "as many tests as possible"

# test for get_input, wordle_game
# get_input, wordle_game -> I/O, move from CLI how?

# ANSI Codes
GREEN  = "\033[42m" + "\033[30m"
YELLOW = "\033[43m" + "\033[30m"
GRAY = "\033[100m"

CLEAR_COL = "\033[0m"

class WordleTest(unittest.TestCase):
    # other "edge cases"?/

    # --- Test for GREEN condition: guess letter in final word, in correct place ---
    def test_green_exact_match(self):
        result = find_match("links", "links")
        for letter in "links":
            self.assertIn(f"{GREEN}{letter}{CLEAR_COL}", result)

    def test_green_single_letter(self):
        result = find_match("links", "lanky")
        self.assertIn(f"{GREEN}n{CLEAR_COL}", result)

    def test_green_duo_letters(self):
        result = find_match("flown", "flier")
        self.assertIn(f"{GREEN}f{CLEAR_COL}", result)
        self.assertIn(f"{GREEN}l{CLEAR_COL}", result)

    def test_green_spaced_letters(self):
       result = find_match("flown", "flaws")
       self.assertIn(f"{GREEN}l{CLEAR_COL}", result)
       self.assertIn(f"{GREEN}w{CLEAR_COL}", result)


    # --- Test for YELLOW condition: guess letter in final word but wrong place ---
    def test_yellow(self):
        result = find_match("nilks", "links")
        self.assertIn(f"{YELLOW}n{CLEAR_COL}", result)

    def test_yellow_single_letter(self):
        result = find_match("nilks", "lanky")
        self.assertIn(f"{YELLOW}n{CLEAR_COL}", result)

    def test_yellow_double_spaced_letter(self):
        result = find_match("damar", "avail")
        self.assertIn(f"{YELLOW}a{CLEAR_COL}", result)
        self.assertIn(f"{YELLOW}a{CLEAR_COL}", result)

    # --- Test for GRAY condition: guess letter not in final word ---
    def test_gray_all(self):
        result = find_match("taxes", "links")
        self.assertIn(f"{GRAY}x{CLEAR_COL}", result)

    def test_gray_single(self):
        result = find_match("lanes", "laner")
        self.assertIn(f"{GRAY}s{CLEAR_COL}", result)

if __name__ == "__main__":
    unittest.main()

    # Run test