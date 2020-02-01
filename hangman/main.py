from tkinter import *
import tkinter.font as font

root = Tk()
default_font = font.Font(family='comic sans ms')
root.geometry("600x400")
root.resizable(width=False, height=False)

# elements

target_word = Label(
  root, font=("comic sans ms",  25), text="_ _ _ _ _ _ _ _ _ _ _"
  )

guess_counter = Label(root, font=("comic sans ms",  25))
new_game = Button(root, text="Start New Game")
new_game['font'] = default_font
easy = Button(root, text='Easy')
hard = Button(root, text='Hard')
user_input = Entry(root)
padding_left_x = Label(root, padx=10)
padding_right_x = Label(root, padx=10)

# draw elements
padding_left_x.grid(row=0, column=0)
target_word.grid(row=1, column=2)
new_game.grid(row=2, column=1)
easy.grid(row=3, column=2)
easy['font'] = default_font
hard.grid(row=3, column=3)
hard['font'] = default_font

# start our program
root.mainloop()