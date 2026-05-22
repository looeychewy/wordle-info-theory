# Building Wordle to kill it with Info Theory
 
## Mechanics
- 6 chances to guess a 5 letter word
- If guess not recognized, reject entry and prompt player to try again w/o losing aa turn
- Hot/cold mechanic (colors to denote letter validity):
  - Green: Letter in answer, in right place
  - Yellow: Letter in answer, in wrong place
  - Grey: Letter not in answer at all
- If letter is guessed more time than appears in answer, extra instances of said letter will show as grey, even if its in the answer otherwise
  - ie Guess 1: Terry, only one R would be colored if R is in the final answer

- If player's guess is entirely green (all letters correct and in right place), game ends in a win
- If all 6 guesses are used without full green, game ends in a loss and correct answer is shown

## Installation
### Requirements
- **Latest version of Python (3.x)**
- Terminals compatible with ANSI (for letter highlighting to work)
### Setup
1. Download wordle.py, guess_pool.csv. Group both files into the same folder
2. Navigate to the folder, open it in your Terminal
2. Run ```python wordle.py``` (Mac: ```python3 wordle.py```)
3. Have fun
