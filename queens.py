'''
Script to solve N queens problem on a NxN chess board.
Example to solve classic 4 queens problem:
import queens
board = queens.Board(N=4)
board.fill()
print(board.solved_states[0])
'''
import numpy as np


class Board:
    '''Contains the current state of the chess board and related functions.'''


    def __init__(self, N):
        '''Class constructor.

        Initialises the board state to be an empty NxN grid.
        The grid is initialised with 0s representing an empty square, and 1s representing a queen (always treated as booleans).

        N : int
            Size of NxN board.
        '''
        self.N = N
        self.state = np.zeros(shape=(N,N), dtype=np.int)
        self.solved_states = list()


    def __str__(self):
        s = self.__repr__() + '\n'
        s += str(self.state) + '\n'
        s += 'number of queens = {}'.format(self.queens)
        return s


    def _queen_valid(self, position):
        '''Tests if it is possible to add a queen to the board at a given postion.

        position : tuple(int, int)
            (i ,j) position to test.
        '''
        # unpack tuble
        i = position[0]
        j = position[1]

        # test row
        if any(self.state[i,:]):
            return False

        # test col
        if any(self.state[:,j]):
            return False

        # test lead diagonal
        if any(self.state.diagonal(offset=j-i)):
            return False

        # test opposite diagonal
        irot = self.N - j - 1
        jrot = i
        if any(np.rot90(self.state).diagonal(offset=jrot - irot)):
            return False

        # queen is valid
        return True


    def _place_queen(self, i):
        # TODO
        raise NotImplementedError()


    def _move_queen(self, i):
        # TODO
        raise NotImplementedError()


    def _delete_queens(self, i):
        # TODO
        raise NotImplementedError()


    def fill(self, k=1, verbosity='low'):
        '''Fill the board with queens.

        k : int (default 1)
            Number of solutions required. If this is bigger than the number of solutions is will return all of the solutions.
            Set to -1 to return all of the solutions.
        verbosity : str (default 'low')
            Verbosity of the solve. if 'low' will solve silently. If 'high' will print ful solve.
        '''
        # TODO
        raise NotImplementedError()


def test_4():
    '''Method to test this works for the standard 4 queens problem'''
    board = Board(N=4)
    print(board)


if __name__ == '__main__':
    test_4()
