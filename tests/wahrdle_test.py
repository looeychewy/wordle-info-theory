import pytest
from unittest.mock import patch, mock_open

from game_files.wordle_two import get_input, render_pattern, wordle_game, WordleGame, CORRECT, PRESENT, ABSENT

# ANSI Codes for use
GREEN = "\033[42m" + "\033[30m"
YELLOW = "\033[43m" + "\033[30m"
GRAY = "\033[100m"
CLEAR_COL = "\033[0m"

class TestFindMatch:
    # --- GREEN TEST CASES ---
    def test_find_match(self):
        assert WordleGame.find_match("flo", "fla") == (CORRECT, CORRECT, ABSENT)

    def test_single_green(self):
        assert WordleGame.find_match("f", "f") == (CORRECT,)

    def test_spaced_green(self):
        assert WordleGame.find_match("flown", "flaws") == (CORRECT, CORRECT, ABSENT, CORRECT, ABSENT)

    # --- YELLOW TEST CASES
    def test_spaced_yellow(self):
        assert WordleGame.find_match("pdpd", "apep") == (PRESENT, ABSENT, PRESENT, ABSENT)

    def test_double_yellow(self):
        assert WordleGame.find_match("appda", "cxspp") == (ABSENT, PRESENT, PRESENT, ABSENT, ABSENT)


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


class TestRenderPattern:
    def test_render_matches_og_colors(self):
        pattern = WordleGame.find_match("flo", "fla")
        assert render_pattern("flo", pattern) == (
            f" {GREEN}f{CLEAR_COL}"
            f" {GREEN}l{CLEAR_COL}"
            f" {GRAY}o{CLEAR_COL}"
        )

class TestWordleGameClass:
    POOL = ["crane", "flown", "flaws", "train", "boxes"]

    def test_game_run(self):
        game = WordleGame(self.POOL, answer="flown")
        assert game.answer == "flown"

    def test_first_try_win(self):
        game = WordleGame(self.POOL, answer="flown")
        game.guess("flown")
        assert game.is_won
        assert game.is_over

    def test_last_chance_win(self):
        game = WordleGame(self.POOL, answer="flown", max_attempts=6)
        for wrong_guess in ["crane", "train", "boxes", "flaws", "crane"]:
            game.guess(wrong_guess)
        assert not game.is_over
        game.guess("flown")
        assert game.is_won
        assert game.is_over

    def test_loss_after_max_attempts(self):
        game = WordleGame(self.POOL, answer="flown", max_attempts=6)
        for _ in range(6):
            game.guess("crane")
        assert game.is_over
        assert not game.is_won