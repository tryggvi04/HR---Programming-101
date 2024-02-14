class Hangman:
    def __init__(self, word: str):
        self.orig_word = word
        self.guessed_letters = ""
        self.format_string = ""
        self.incorrect_counter = 0
        
    def guess_letter(self, letter: str) -> bool:
        letter = letter.upper()
        if letter in self.guessed_letters:
            return False

        if letter in self.orig_word.upper():
            self.guessed_letters += letter
            return True
        else:
            self.incorrect_counter += 1
            self.guessed_letters += letter  
            return False  
    def __str__(self) -> str:
        self.format_string = ""
        for char in self.orig_word:
            if char.upper() in self.guessed_letters:
                self.format_string += char.upper() + " "
            elif char.isalpha():
                self.format_string += "_ "
            else:
                self.format_string += char
        return "{}\nNumber of incorrect guesses: {}".format(self.format_string.strip(), self.incorrect_counter)



        