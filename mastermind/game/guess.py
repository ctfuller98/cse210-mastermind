class Guess():
    
    def __init__(self):
        self.guess = ""

    def set_guess(self, input_guess):
        self.guess = input_guess

    def get_guess(self):
        return self.guess