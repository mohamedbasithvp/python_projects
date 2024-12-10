import math
import random

from wx.lib.masked import value


class Player:
    def __init__(self, letter):
        # letter is x or o
        self.letter=letter

    # we want all players to get their next move given a game
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # get a random valid spot for our next move
        square=random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_Square = False
        val = None
        while not valid_Square:
            square=input(self.letter + '\'s turn. input move (0-8):')
            # we're going to check that this is a currect value by trying to cast.
            # it to an integer. and if it is not, then we say its invalid
            # if that spot is not available on the board, we also say its invalid

            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_Square=True # if these are successful, then yay!
            except ValueError:
                print('Invalid square. Try again.')
        return val