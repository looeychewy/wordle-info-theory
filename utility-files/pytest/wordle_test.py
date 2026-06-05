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


# mock to test wordle_game + get_input