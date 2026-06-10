# Help import functions from /game_files/wordle.py...?
# import sys
# sys.path.insert(0, "../game_files")

import pytest
from unittest.mock import patch
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


# MOCKS (to test wordle_game + get_input) Class TestGetInput
# get_input(_input here_) -> waits for input, rethink this

class TestGetInput:
    @patch('builtins.input', return_value="FLOWN")
    def test_get_input(self, mock_get):
        result = get_input("")
        assert result == "flown"

    @patch('builtins.input', return_value="F")
    def test_single_input(self, mock_get):
        result = get_input("")
        assert result == "f"

        # use pytest -s for now
        # how bind "flo" to get_input? -> result = get_input("flo") does not work like that




# @patch('game_files.wordle.wordle_game')
# def test_wordle_game():
#     pass