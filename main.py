import numpy as np
from game.game import Game

game = Game(4)

# game.board = np.array([[1,2,3,4],[3,4,1,2,],[2,3,4,1],[4,1,2,3]])
game.board = np.array([[1,2,3,4],[0,4,0,2,],[2,3,0,1],[0,1,2,3]])

game.create_blocks()

print(game.board)

output = game.simple_solve()

print(output)





game = Game()
game.board = np.array([[0,2,0,4,5,6,7,8,9],[4,5,7,0,8,0,2,3,6],[6,8,9,2,3,7,0,4,0],[0,0,5,3,6,2,9,7,4],[2,7,4,0,9,0,6,5,3],[3,9,6,5,7,4,8,0,0],[0,4,0,6,1,8,3,9,7],[7,6,1,0,4,0,5,2,8],[9,3,8,7,2,5,0,6,0]])
game.create_blocks()

print(game.board)
output = game.simple_solve()

print(output)





# game = Game(3)

# board = game.board
# size = game.size

# for i in range(0, size):
#     for j in range(0, size - 1):
#         pre = (i + j + 1)
#         num = pre if pre % size == 0 else pre % size 
#         board[i][j] = num

# print(board)
# print(board.T)

# output = game.simple_solve()

# print(output)
# print(0 in output)

