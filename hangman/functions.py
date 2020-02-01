class HmFunctions:

    def show_length(self, word):  # This returns the length of the word as under scores _ _ _
        length = ""

        for letter in range(0, len(word)):
            length += '_ '

        return length

    # This checks that the user input doesn't contain a number
    def check_for_digits(self, word):
        return any(word.isdigit() for char in word)

    # This checks if the letter is in the word.
    def check_letters(self, word, letter):
        return letter in word

    # This checks the new guess and sends back a new dict
    def update_correct_letters(self, letter, word):
        placements = {}
        for i in range(0, len(word)):
            if word[i] == letter:
                placements[i] = letter
        return placements

    # This returns a new string with the correct letters: C _ R _
    def update_readable_length(self, letters, word):
        updated_word = ''
        updated = False

        for i in range(0, len(word)):
            for k, v in letters.items():
                if k == i:
                    updated_word += v + ' '
                    updated = not updated

            if not updated:
                updated_word += '_ '
            else:
                updated = not updated
        return updated_word

    # This checks to see if the word is complete.
    def check_win(self, letters, _word):
        word = self.update_readable_length(letters, _word)
        if '_' in word:
            return False
        else:
            return True

    def announce_win(self):

        # this block can be converted to a function not DRY
        print('WINNER!!!!!')
        play_again = input('Do you want to play again: ')

        if 'y' not in play_again.lower():
          return False
        else:
          return True

    def show_help(self, guess, correct_letters, word, counter, guessed_letters):
        # Convert this block to function, just cause messy..
        if guess.lower() == 'quit':
            print('quitting')
            return True
        elif guess.lower() == 'view':
            print(self.update_readable_length(correct_letters, word))
        elif guess.lower() == 'help':
            print('Quit: quit ')
            print('View: view the correct letters so far.')
            print('Count: view your total number of guesses so far.')
            print('Letters: Show all the letters you\'ve tried so far.')
        elif guess.lower() == 'count':
            print(f'So far you\'ve had {counter} guesses.')
        elif guess.lower() == 'letters':
            letters = ''
            for i in range(len(guessed_letters)):
                letters += guessed_letters[i] + ' '
            print(f'Your guessed letters so far are: {letters}')
        else:
            print('Ermmmm you drunk? 😁')

