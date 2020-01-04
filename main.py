import numpy as np


# parameters
N = 4   # the chess board is NxN
Q = 4   # there are Q queens to be placed on the board


class Board:
    '''Contains the current state of the chess board and related functions'''

    def __init__(self, N, Q):
        '''Class constructor

        Initialises the board state to be an empty NxN grid along with the number of queens to be placed.
        The grid is initialised with 0s representing an empty square, and 1s representing a queen (always treated as booleans)

        N : int
            Size of NxN board
        Q : int
            Number of queens to be placed
        '''
        self.state = np.zeros(shape=(N,N), dtype=np.int)
        self.queens = Q

    def __str__(self):
        s = self.__repr__() + '\n'
        s += str(self.state) + '\n'
        s += 'number of queens = {}'.format(self.queens)
        return s


b = Board(4, 4)
print(b)
