# Building Wordle to kill it with Info Theory
 
## Mechanics:
- 6 chances to guess a 5 letter word
- Preset **answer pool** derived from larger valid English **guess pool**
    - If guess not recognized, reject entry and prompt player to try again w/o losing aa turn
- Hot/cold mechanic (colors to denote letter validity):
  - Green: Letter in answer, in right place
  - Yellow: Letter in answer, in wrong place
  - Grey: Letter not in answer at all
- Keyboard always reflects best color has received across all guesses
  - ie Guess 1: letter Y is yellow, Guess 2: letter Y is now green and stays green
- If letter is guessed more time than appears in answer, extra instances of said letter will show as grey, even if its in the answer otherwise
  - ie Guess 1: Terry, only one R would be colored if R is in the final answer

- If player's guess is entirely green (all letters correct and in right place), game ends in a win
- If all 6 guesses are used without full green, game ends in a loss and correct answer is shown
