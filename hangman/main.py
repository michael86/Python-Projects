from functions import HmFunctions
from words import WordGenerator
import tkinter as tk
import tkinter.font as font
from PIL import ImageTk, Image

function = HmFunctions()
word_generator = WordGenerator()

new_word = word_generator.generate_new_word()

# Set up the root window.
root = tk.Tk()  # Initialise root GUI
root.configure(background='black')
root.title("Hangman")
default_font = font.Font(family='comic sans ms')  # Set default font to comic sans
root.geometry("600x400")  # Set our gui width and height
root.resizable(width=False, height=False)  # Set resizable to False

# Create our canvas
canvas = tk.Canvas(root, height=400, width=600)
canvas.pack()

# Create our image, resembling background.
photo = ImageTk.PhotoImage(Image.open("background_image.jpg"))  # Import bg image
background_label = canvas.create_image((0, 0), image=photo, anchor=tk.N+tk.W)

# Display our target word as underscores.
target_word = canvas.create_text(
  (300, 40), font=("comic sans ms",  25), text=function.show_length(new_word), fill='white'
  )

guess_counter = tk.Label(root, font=("comic sans ms",  25))
new_game = tk.Button(root, text="Start New Game")
new_game['font'] = default_font
easy = tk.Button(root, text='Easy')
hard = tk.Button(root, text='Hard')
user_input = tk.Entry(root)
padding_left_x = tk.Label(root, padx=10)
padding_right_x = tk.Label(root, padx=10)

# start our program
root.mainloop()
