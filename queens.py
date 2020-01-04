'''Script to solve N queens problem on a NxN chess board.'''
import numpy as np


class Board:
    '''Contains the current state of the chess board and related functions.'''


    def __init__(self, N):
        '''Class constructor.

        Initialises the board state to be an empty NxN grid.
        The grid is initialised with 0s. 0s representing an empty square, and 1s representing a queen (always treated as booleans).

        N : int
            Size of NxN board.
        '''
        self.N = N
        self.state = np.zeros(shape=(N,N), dtype=np.int)


    def __str__(self):
        return str(self.state) + '\n'


    def _queen_valid(self, position):
        '''Tests if it is possible to add a queen to the board at a given postion.

        position : tuple(int, int)
            (i ,j) position to test.

        returns : bool
            Bool indicating if queen is valid in this postion.
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


    def _place_queen(self, j):
        '''Attempts to place a queen in column j.

        j : int
            Column to attempt to place queen.

        returns : bool
            Bool indicating if placing of queen was succesfull.
        '''
        for i in range(self.N):
            if self._queen_valid((i, j)):
                self.state[i,j] = 1
                return True
        return False


    def _move_queen(self, j):
        '''Attempts to move a queen down in column j.

        j : int
            Column to attempt to move queen down.

        returns : bool
            Bool indicating if moving of queen was succesfull.
        '''
        current_index = int(np.where(self.state[:,j])[0][0])
        self.state[current_index,j] = 0
        for i in range(current_index + 1, self.N):
            if self._queen_valid((i, j)):
                self.state[i,j] = 1
                return True
        self.state[current_index,j] = 1
        return False


    def _delete_queens(self, j):
        '''Delete all queens to the right of and including column j.

        j : int
            Column to begin deletion.
        '''
        for col in range(j, self.N):
            self.state[:,col] = 0


    def _solve_col(self, j):
        '''Solve column j.

        j : int
            Column to solve.
        '''
        for col in range(j, self.N):
            assert all(self.state[:,col] == 0)
        if j == self.N:
            return
        if self._place_queen(j):
            self._solve_col(j+1)
        else:
            if self._move_queen(j-1):
                self._solve_col(j)
            else:
                self._ripple(j)


    def _ripple(self, j):
        '''Ripple column j.

        This is called when the current column is unsolvable, this resets the previous column and retries.

        j : int
            Column to ripple.
        '''
        self._delete_queens(j-1)
        if self._move_queen(j-2):
            self._solve_col(j-1)
        else:
            self._ripple(j-1)


    def fill(self):
        '''Fill the board with queens.'''
        solve = self._solve_col(0)


def solve(N):
    '''Method to sovle the N queens problem'''
    board = Board(N)
    print('solving {} queens problem...'.format(N))
    board.fill()
    print(board.state)


if __name__ == '__main__':
    N = int(input('N = '))
    solve(N)
