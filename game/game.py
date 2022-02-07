import numpy as np
from math import sqrt

class Game():
    def __init__(self, size=9):
        self.size = size
        self.board = np.zeros((size, size))
        # a range of the numbers that can appear on the board
        self.options = np.arange(1, size + 1)
        # self.num_blocks = int(sqrt(size))
        self.blocks = None
        self.block_mapping = {}


    def create_blocks(self) -> np.ndarray:
        blocks = np.zeros((self.size, self.size))
        root = int(sqrt(self.size))
        mover_right = 0
        mover_down = 0
        for i in range(self.size):
            self.block_mapping[i] = {}
            counter = 0
            for x in range(mover_down, root + mover_down):
                for y in range(mover_right, root + mover_right):
                    blocks[i][counter] = self.board[x][y]
                    self.block_mapping[i][counter] = (x, y)
                    counter += 1
            if (i + 1) % root == 0:
                mover_right = 0
                mover_down += root
            else:
                mover_right += root
        
        self.blocks = blocks
        # print(self.block_mapping)
        return blocks        

    
    def put_number(self, row: int, column: int, number: int, board: np.ndarray) -> np.ndarray:
        # get_possibilites is 1-indexed not 0 but board is 0 indexed so adjust
        board[row - 1][column - 1] = number
        return board


    def get_row_column_intersection(self, row, column, board) -> np.ndarray:
        row -= 1
        column -= 1
        row_possibilities = np.setdiff1d(self.options, board[row])
        column_possibilites = np.setdiff1d(self.options, board.T[column])
        intersection = np.intersect1d(row_possibilities, column_possibilites)
        return intersection

    
    def get_block_intersection(self, block_num: int) -> tuple:
        if self.blocks is None:
            return None
        block_possibilities = np.setdiff1d(self.options, self.blocks[block_num])
        if block_possibilities.size == 1:
            value = block_possibilities[0]
            i = np.where(self.blocks[block_num]==0)[0][0]
            board_index = self.block_mapping[block_num][i]
            # return ((x,y), v)
            return board_index, value
        else:
            return None



    def simple_solve(self) -> np.ndarray:
        board_copy = np.copy(self.board)
        updated = True
        while updated:
            updated = False
            for r in range(1, self.size + 1):
                for c in range(1, self.size + 1):
                    if board_copy[r-1][c-1] == 0:
                        possiblilites = self.get_row_column_intersection(r, c, board_copy)
                        if possiblilites.size == 1:
                            self.put_number(r, c, possiblilites[0], board_copy)
                            updated = True
            self.create_blocks()
            for b in range(self.size):
                output = self.get_block_intersection(b)
                if output is not None:
                    coordinates, value = output
                    r = coordinates[0] + 1
                    c = coordinates[1] + 1 
                    if board_copy[r-1][c-1] == 0:
                        self.put_number(r, c, value, board_copy)
                        updated = True
            self.create_blocks()
            # print(board_copy)
        solved = False
        if 0 not in board_copy:
            solved = True
        return board_copy, solved