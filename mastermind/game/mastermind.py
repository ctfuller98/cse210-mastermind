import numpy

class Mastermind:
    def __init__(Self):
        # Dictionary that stores player codes by name
        Self._codes = {}
        Self._code_length = 4
        Self._last_guess_correct = False
    
    def generate_codes(Self, player_names):
        for name in player_names:
            if name in Self._codes:
                print("Duplicate name detected, this is going to cause errors, but we're too lazy to fix it")
            Self._codes[name] = numpy.random.randint(0, high=9, size=Self._code_length)
    
    def check_guess(Self, guess):
        assert len(guess.get_code()) == Self._code_length, "code lengths must match"
        # number correct and in right position
        correct = 0
        # number correct but not in right position
        close = 0
        code = guess.getName()
        guess_code = guess.get_code()
        for gindex in range(Self._code_length):
            for cindex in range(Self._code_length):
                if code[cindex] == guess_code[gindex]:
                    if gindex == cindex:
                        correct += 1
                    else:
                        close += 1
        if (correct == Self._code_length):
            Self._last_guess_correct = True
        else:
            Self._last_guess_correct = False
        return "X" * correct + "*" * close + "O" * (Self._code_length - correct - close)
    
    def last_guess_correct(Self):
        return Self._last_guess_correct
    

if __name__ == "__main__":
    #Testing code that only runs if we run this file indipendently
    m = Mastermind()
    m.generate_codes(["Eli", "Eli", "Braxton", "Cameron", "Dallin"])
    # Turns out this isn't private, we just pretend
    print(m._codes)
    #print(m.check_guess([1,2,3,4]))

    