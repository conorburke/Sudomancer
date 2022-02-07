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
    game.put_number(row=1, column=1, number=3)
    game.board[0][0] = 3


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

    assert np.array_equal(game.get_possibilities(1, 3), np.array([3]))
    assert np.array_equal(game.get_possibilities(2, 3), np.array([1]))
    assert np.array_equal(game.get_possibilities(3, 3), np.array([2]))


def test_solve():
    game = Game(3)

    board = game.board
    size = game.size

    for i in range(0, size):
        for j in range(0, size - 1):
            pre = (i + j + 1)
            num = pre if pre % size == 0 else pre % size 
            board[i][j] = num 

    game.solve()
    
    solved = np.array([[1,2,3],[2,3,1],[3,1,2]])


    assert np.array_equal(game.board, solved)