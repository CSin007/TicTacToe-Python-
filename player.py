import math
import random

class Player:
    def __init__(self,XorO):
        self.letter=XorO

        def get_move(self,game):
            pass

class RandomComputerPlayer(Player):
            def __init__(self,XorO):
                super().__init__(XorO)

            def get_move(self,game):
                squarespot=random.choice(game.available_moves())
                return squarespot

class HumanPlayer(Player):
    def __init__(self,XorO):
     super().__init__(XorO)

    def get_move(self,game):
        valid_square=Falseval=None
        while not valid_square:
            square=input(self.letter + '\'s turn. Input move(0-8) : ')
            try:
                valuenew=int(square)
                if valuenew not in game.available_moves():
                    raise ValueError
                valid_square=True
            except ValueError:
                print(' Invalid square. Try again.')

        return valuenew


