"""
Super basic keyboard GUI app with tkinter -> utilize for actual Wordle keyboard hopefully
- Enter/Del functionality needs to be implemented (shows up as words currently)
    - Del functionality done 4/15
    - Enter WIP
- Limit text entered FROM KEYBOARD to 5 characters
- Link IRL keyboard to actually type on the screen without needing to click into the Entry box
    - display.focus_set() -> done 4/15
- Capitalized input into Entry widget
    - Done 4/17
"""

import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("Wordle Keyboard")
root.configure(background="Dark grey")
root.geometry("1260x500+150+200") # +[VALUE] sets on-screen pos., x & y respectively
root.resizable(False, False)

# Sets main title for the application window
main_title = Label(root, width=39, bg='Dark Grey', font=('arial', 40, 'bold'), text='\tWordle Keyboard\t', padx=12)
main_title.grid(row=0, column=0)

# Container to hold + organize all keyboard buttons
main_frame = Frame(root, bg ='Dark Grey', bd = 10, width = 1250, height = 490, relief="flat")
main_frame.grid(row = 2, column = 0, padx = 100, pady = 30)

# Contains labels for all buttons, draws directly from str element here to feed into the display (text = key)
keys = [ ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
         ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
         ['ENTER', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', 'DEL', 'CLEAR'] # How implement ENTER & DEL functionality?
]


# Converts keyboard input into uppercase letters
def uppercase_conversion(*args):
    display_text.set(display.get().upper())

# Display outputted text (Entry object)
display_text = StringVar()
display = tk.Entry(root, textvariable = display_text, font=('arial', 28), bd = 5, width = 54)
display.focus_set() # Able to type into Entry widget without first clicking on it

display_text.trace('w', uppercase_conversion)
display.grid(row = 1, column = 0, columnspan = len(keys[0]), pady = 10)

for i, key_row in enumerate(keys):
    for j, key in enumerate(key_row):
        kb_buttons = (tk.Button(main_frame, font = ('arial', 14), text = key, width = 7, height = 2, command = lambda key = key:
                  button_click(key)).grid(row = i+2, column = j))

# Main button click functionality
def button_click(kb_key):
    if kb_key == 'DEL':
        display.delete(len(display.get()) - 1, 'end')
    elif kb_key == 'ENTER':
        display.delete(0, tk.END)
        display.insert(0, str("String passed")) # placeholder for finalized enter functionality
    elif kb_key == 'CLEAR':
        display.delete(0, tk.END)
    else:
        current = display.get()
        display.delete(0, tk.END)
        display.insert(0, str(current) + str(kb_key))

        # Basic character entry limit (irl keyboard input not limited yet)
        if len(display.get()) > 5:
            display.delete(5, END)


root.mainloop()