from words import WordGenerator
from functions import HmFunctions
from tkinter import *

# root = Tk()
# name = Label(root, text = "Hi ")
# name.grid(row=0, column=0)
# user_input = Entry(root).grid(row=0, column=1)
#
# root.mainloop()

function = HmFunctions()  # bunch of functions
gw = WordGenerator()  # This generates a random word.
word = gw.generate_new_word()  # Target word
won = False  # Allow us to enter first while loop

print(word)

print('''
WELCOME TO HANGMAN....
Guess the word in as least attempts as possible.
To view all the commands available type 'Help' at any time.' 
        
''' + function.show_length(word))

guess = None

correct_letters = {}  
guessed_letters = [] 
counter = 0 

while not won or guess is None:

    guess = input('\nTake a guess: ')

    if guess not in guessed_letters:  # Check if a Char.

        if len(guess) == 1:  
            
            guessed_letters.append(guess)
            guessed_letters.sort()
            counter += 1

            if function.check_letters(word, guess.lower()):
                print('that letter was there')

                new_letters = function.update_correct_letters(guess, word)  # update local dict of correct letters.

                for k, v in new_letters.items():
                    correct_letters[k] = v  # Update local dictionary with new key and value.

                print(function.update_readable_length(correct_letters, word))

                if function.check_win(correct_letters, word):
                    if not function.announce_win():
                        won = not won
                    else:
                        correct_letters = {}  # Clear both for new game.
                        guessed_letters = []
                        word = gw.generate_new_word()  # Generate new word.
                        print(f'New game\n{function.show_length(word)}')
                        
            else:
                print('bad luck')            
        elif guess == word:  
            
            if not function.announce_win():
                won = not won
            else:
                correct_letters = {}  # Clear both dicts for new game.
                guessed_letters = []
                word = gw.generate_new_word()  # Generate new word.
                print(f'New game\n{function.show_length(word)}')
        else:
            if function.show_help(guess, correct_letters, word, counter, guessed_letters):
                # This function only returns True if guess == quit
                break
    else:
        print(f'You\'ve already tried {guess}')
else:
    if not won:
        print(f'Well done, you broke something..... {guess}')
