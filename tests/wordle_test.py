# Help import functions from /game_files/wordle.py...?
# import sys
# sys.path.insert(0, "../game_files")

import pytest
from unittest.mock import patch, MagicMock
from game_files.wordle import find_match, wordle_game, get_input

# ANSI Codes for use
GREEN  = "\033[42m" + "\033[30m"
YELLOW = "\033[43m" + "\033[30m"
GRAY = "\033[100m"

CLEAR_COL = "\033[0m"


class TestFindMatch:
    # ---- GREEN TEST CASES ----
    def test_find_match(self):
        assert find_match("flo", "fla") == f" {GREEN}f{CLEAR_COL}" f" {GREEN}l{CLEAR_COL}" f" {GRAY}o{CLEAR_COL}"

    def test_single_green(self):
        assert find_match("f", "f") == f" {GREEN}f{CLEAR_COL}"

    def test_spaced_green(self):
        assert find_match("flown", "flaws") == f" {GREEN}f{CLEAR_COL}" f" {GREEN}l{CLEAR_COL}" f" {GRAY}o{CLEAR_COL}" f" {GREEN}w{CLEAR_COL}" f" {GRAY}n{CLEAR_COL}"

    # ---- YELLOW TEST CASES ----
    def test_spaced_yellow(self):
        assert find_match("pdpd", "apep") == f" {YELLOW}p{CLEAR_COL}" f" {GRAY}d{CLEAR_COL}" f" {YELLOW}p{CLEAR_COL}" f" {GRAY}d{CLEAR_COL}"


# MOCKS (to test get_input + wordle_game)
class TestGetInput:
    @patch('builtins.input', return_value="FLOWN") # return_value is what gets pushed as a mock
    def test_all_caps_input(self, mock_get):
        result = get_input("")
        assert result == "flown"

    @patch('builtins.input', return_value="fLoWN")
    def test_mixed_case_input(self, mock_get):
        result = get_input("")
        assert result == "flown"

    @patch('builtins.input', return_value="F")
    def test_single_input(self, mock_get):
        result = get_input("")
        assert result == "f"

# class TestWordleGame -> test various scenarios not the entire broad category
# also the fuckin repo isnt updated shit
# HAVE TO MOCK -> file I/O, input, .random()
    # scenarios: test csv pulling,
        # lowk might just be tired but i dont see the need to fully test every bit of wordle_game()
class TestWordleGame:
    pass

