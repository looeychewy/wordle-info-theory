from unittest.mock import patch, mock_open
from unittest.mock import MagicMock
from game_files.wordle import get_input, find_match, wordle_game

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

    def test_double_yellow(self):
        assert find_match("appda", "cxspp") == f" {GRAY}a{CLEAR_COL}" f" {YELLOW}p{CLEAR_COL}" f" {YELLOW}p{CLEAR_COL}" f" {GRAY}d{CLEAR_COL}" f" {GRAY}a{CLEAR_COL}"

# MOCKS (to test get_input + wordle_game)
class TestGetInput:
    @patch('builtins.input', return_value="FLOWN") # return_value is what gets pushed as a mock
    def test_all_caps_input(self, _):
        result = get_input("")
        assert result == "flown"

    @patch('builtins.input', return_value="fLoWN")
    def test_mixed_case_input(self, _):
        result = get_input("")
        assert result == "flown"

    @patch('builtins.input', return_value="F")
    def test_single_input(self, _):
        result = get_input("")
        assert result == "f"

# HAVE TO MOCK -> file I/O, input, .random()
# test win conditions (first word win, last chance win, no chances loss)
#TODO: WORDLE_GAME TEST SUITE
class TestWordleGame:
    # Preset testing answer pool
    FAKE_CSV = "crane\nflown\nflaws\ntrain\nboxes"

    @patch('builtins.print')
    @patch('builtins.open')
    @patch('builtins.input')
    @patch('random.choice')
    def test_first_try_win(self, mock_choice, mock_input, mock_open_, mock_print):
        mock_choice.return_value = "flown" # mock random choice
        mock_input.return_value = "flown" # mock user input
        mock_open_.return_value = mock_open(read_data=self.FAKE_CSV)() # mock grabbing from the csv

        wordle_game()
         #'

        pass


