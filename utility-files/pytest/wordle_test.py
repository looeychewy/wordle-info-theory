# Pytest for wordle.py -> syntax..?
# pytest command not found -> uv
# coverage run -m pytest
# pytest --cov=myproj tests/

import pytest
from wordle_game import find_match

# ANSI Codes
GREEN  = "\033[42m" + "\033[30m"
YELLOW = "\033[43m" + "\033[30m"
GRAY = "\033[100m"

CLEAR_COL = "\033[0m"



# find_match(play_guess, final_answer)
def test_find_match():
    assert find_match("flo", "fla") == f" {GREEN}f{CLEAR_COL}" f" {GREEN}l{CLEAR_COL}" f" {GRAY}o{CLEAR_COL}"

def test_spaced_green():
    assert find_match("flown", "flaws") == f" {GREEN}f{CLEAR_COL}" f" {GREEN}l{CLEAR_COL}" f" {GRAY}o{CLEAR_COL}" f" {GREEN}w{CLEAR_COL}" f" {GRAY}n{CLEAR_COL}"


