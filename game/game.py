from typing import Tuple
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
        # {block_row: {block_row_index: (board_row, board_column)}}
        self.block_to_coordinate_mapping = {}
        # {(board_row, board_column): block_row}
        self.coordinate_to_block_mapping = {}


    def create_blocks(self, board: np.ndarray) -> np.ndarray:
        blocks = np.zeros((self.size, self.size))
        root = int(sqrt(self.size))
        mover_right = 0
        mover_down = 0
        for i in range(self.size):
            self.block_to_coordinate_mapping[i] = {}
            counter = 0
            for x in range(mover_down, root + mover_down):
                for y in range(mover_right, root + mover_right):
                    blocks[i][counter] = board[x][y]
                    self.block_to_coordinate_mapping[i][counter] = (x, y)
                    self.coordinate_to_block_mapping[(x,y)] = i
                    counter += 1
            if (i + 1) % root == 0:
                mover_right = 0
                mover_down += root
            else:
                mover_right += root
        
        self.blocks = blocks
        return blocks        

    
    def user_put_number(self, row: int, column: int, number: int, board: np.ndarray) -> np.ndarray:
        """ Don't require use to think about zero-indexing """
        return self.put_number(row - 1, column - 1, number, board)

    
    def put_number(self, row: int, column: int, number: int, board: np.ndarray) -> np.ndarray:
        board[row][column] = number
        return board


    def get_block_from_coordinates(self, x: int, y: int) -> int:
        return self.coordinate_to_block_mapping[(x, y)]


    def get_row_column_intersection(self, row, column, board) -> np.ndarray:
        row_possibilities = np.setdiff1d(self.options, board[row])
        column_possibilites = np.setdiff1d(self.options, board.T[column])
        intersection = np.intersect1d(row_possibilities, column_possibilites)
        return intersection

    
    def get_block_intersection(self, block_num: int) -> tuple:
        if self.blocks is None:
            return None
        # block_possibilities = np.setdiff1d(self.options, self.blocks[block_num])
        block_possibilities = self.get_block_possibilites(block_num, self.blocks)
        if block_possibilities.size == 1:
            value = block_possibilities[0]
            i = np.where(self.blocks[block_num]==0)[0][0]
            board_index = self.block_to_coordinate_mapping[block_num][i]
            # return ((x,y), v)
            return board_index, value
        else:
            return None

    
    def get_block_possibilites(self, block_num: int, blocks: np.ndarray) -> np.ndarray:
        return np.setdiff1d(self.options, blocks[block_num])



    def simple_solve(self) -> np.ndarray:
        board_copy = np.copy(self.board)
        updated = True
        while updated:
            updated = False
            for r in range(0, self.size):
                for c in range(0, self.size):
                    if board_copy[r][c] == 0:
                        possiblilites = self.get_row_column_intersection(r, c, board_copy)
                        if possiblilites.size == 1:
                            self.put_number(r, c, possiblilites[0], board_copy)
                            updated = True
            self.create_blocks(board_copy)
            for b in range(self.size):
                output = self.get_block_intersection(b)
                if output is not None:
                    coordinates, value = output
                    r = coordinates[0]
                    c = coordinates[1] 
                    if board_copy[r][c] == 0:
                        self.put_number(r, c, value, board_copy)
                        updated = True
            self.create_blocks(board_copy)
        solved = False
        if 0 not in board_copy:
            solved = True
        return board_copy, solved

    
    def recursive_solve(self, board: np.ndarray, board_size: int) -> Tuple[np.ndarray, bool]:
        if 0 not in board:
            return board, True
        for r in range(0, board_size):
            for c in range(0, board_size):
                if board[r][c] == 0:
                    blocks = self.create_blocks(board)
                    row_column_possibilities = self.get_row_column_intersection(r, c, board)
                    current_block = self.get_block_from_coordinates(r, c)
                    block_possibilities = self.get_block_possibilites(current_block, blocks)
                    row_column_block_possiblilites = np.intersect1d(row_column_possibilities, block_possibilities)
                    for p in row_column_block_possiblilites:
                        board_copy = np.copy(board)
                        self.put_number(r, c, p, board_copy)
                        output_board, is_solved = self.recursive_solve(board_copy, board_size)
                        if is_solved:
                            return output_board, is_solved
                    return board, False
