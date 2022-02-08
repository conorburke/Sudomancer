import numpy as np
from game.game import Game

def test_board_dimensions():
    game = Game()
    assert game.board.shape == (9,9)

    game = Game(size=3)
    assert game.board.shape == (3,3)


def test_set_number():
    game = Game(3)
    # user should not have to use zero index
    game.user_put_number(row=1, column=1, number=3, board=game.board)
    assert game.board[0][0] == 3


def test_create_blocks():
    game = Game(4)
    game.board = np.array([[1,2,3,4],[3,4,1,2,],[2,3,4,1],[4,1,2,3]])
    game.create_blocks(game.board)
    
    expected_blocks = np.array([[1,2,3,4], [3,4,1,2], [2,3,4,1], [4,1,2,3]])

    assert np.array_equal(game.blocks, expected_blocks)


def test_coordinate_to_block_mapping():
    game = Game(4)
    game.board = np.array([[1,2,3,4],[3,4,1,2,],[2,3,4,1],[4,1,2,3]])
    game.create_blocks(game.board)

    assert game.coordinate_to_block_mapping[(1,1)] == 0
    assert game.coordinate_to_block_mapping[(0,2)] == 1
    assert game.coordinate_to_block_mapping[(2,0)] == 2
    assert game.coordinate_to_block_mapping[(2,2)] == 3

def test_number_options():
    game = Game()

    options = np.array([1,2,3,4,5,6,7,8,9])
    assert np.array_equal(game.options, options)


def test_possibilities():
    game = Game(3)

    board = game.board
    size = game.size

    for i in range(0, size):
        for j in range(0, size - 1):
            pre = (i + j + 1)
            num = pre if pre % size == 0 else pre % size 
            board[i][j] = num

    assert np.array_equal(game.get_row_column_intersection(0, 2, board), np.array([3]))
    assert np.array_equal(game.get_row_column_intersection(1, 2, board), np.array([1]))
    assert np.array_equal(game.get_row_column_intersection(2, 2, board), np.array([2]))


def test_simple_solve_mini():
    game = Game(3)

    board = game.board
    size = game.size

    for i in range(0, size):
        for j in range(0, size - 1):
            pre = (i + j + 1)
            num = pre if pre % size == 0 else pre % size 
            board[i][j] = num 

    output = game.simple_solve()
    board_output, is_solved = output
    
    solved = np.array([[1,2,3],[2,3,1],[3,1,2]])


    assert np.array_equal(board_output, solved)
    assert is_solved


def test_simple_solve_9x9():
    game = Game()
    game.board = np.array([[0,0,0,4,5,0,7,0,0],[0,0,0,0,8,0,2,3,6],[0,0,9,2,0,7,0,4,0],[0,0,5,0,0,0,9,0,4],[2,7,4,0,0,0,6,0,3],[3,9,0,5,0,0,8,0,0],[0,4,0,0,1,0,0,9,7],[7,0,1,0,4,0,5,0,8],[9,3,8,0,2,0,0,6,0]])
    game.create_blocks(game.board)
    output_board, is_solved = game.simple_solve()
    print(output_board)
    assert is_solved


def test_recursive_solve_9x9():
    game = Game()
    game.board = np.array([[0,0,0,0,5,0,7,0,0],[0,0,0,0,8,0,2,3,6],[0,0,9,0,0,7,0,4,0],[0,0,5,0,0,0,9,0,4],[2,7,4,0,0,0,6,0,3],[3,9,0,5,0,0,8,0,0],[0,4,0,0,1,0,0,9,7],[7,0,1,0,4,0,5,0,8],[9,3,8,0,2,0,0,6,0]])
    game.create_blocks(game.board)
    output_board, is_solved = game.simple_solve()
    output_board, is_solved = game.recursive_solve(output_board, 9)
    print(output_board)
    assert  is_solved

def test_recursive_solve_blank_board_9x9():
    game = Game()
    game.board = np.array([[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]])
    game.create_blocks(game.board)
    output_board, is_solved = game.simple_solve()
    output_board, is_solved = game.recursive_solve(output_board, 9)
    print(output_board)
    assert is_solved


def test_supposed_hardest_sudoku_ever():
    game = Game()
    game.board = np.array([[8,0,0,0,0,0,0,0,0],[0,0,3,6,0,0,0,0,0],[0,7,0,0,9,0,2,0,0],[0,5,0,0,0,7,0,0,0],[0,0,0,0,4,5,7,0,0],[0,0,0,1,0,0,0,3,0],[0,0,1,0,0,0,0,6,8],[0,0,8,5,0,0,0,1,0],[0,9,0,0,0,0,4,0,0]])
    game.create_blocks(game.board)
    output_board, is_solved = game.simple_solve()
    output_board, is_solved = game.recursive_solve(output_board, 9)
    print(output_board)
    assert is_solved