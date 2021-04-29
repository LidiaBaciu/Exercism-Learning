# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = word
        self.to_be_guessed = set(word)

    def guess(self, char):
        if self.status != STATUS_ONGOING:
            raise ValueError('Game finished')

        if char in self.to_be_guessed:
            self.to_be_guessed.remove(char)
            if not self.to_be_guessed:
                self.status = STATUS_WIN
                
        else:
            self.remaining_guesses -= 1
            if self.remaining_guesses < 0 :
                self.status = STATUS_LOSE
        return

    def get_masked_word(self):
        return "".join("_" if c in self.to_be_guessed else c for c in self.word)

    def get_status(self):
        return self.status