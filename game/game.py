import numpy as np

class Game():
    def __init__(self, size=9):
        self.size = size
        self.board = np.zeros((size, size))
        self.options = np.arange(1, size + 1)

    def put_number(self, row, column, number):
        spot = self.board[row - 1][column - 1]
        spot = number

    def get_possibilities(self, row, column) -> np.array:
        row -= 1
        column -= 1
        row_possibilities = np.setdiff1d(self.options, self.board[row])
        column_possibilites = np.setdiff1d(self.options, self.board.T[column])
        intersection = np.intersect1d(row_possibilities, column_possibilites)
        return intersection

    def solve(self):
        updated = True
        while updated:
            updated = False
            for r in range(1, self.size + 1):
                for c in range(1, self.size + 1):
                    possiblilites = self.get_possibilities(r, c)
                    if possiblilites.size == 1:
                        self.board[r - 1][c - 1] = possiblilites[0]
                        updated = True
