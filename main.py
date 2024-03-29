import numpy as np
from game.game import Game

# play hardest game and print result
game = Game()
game.board = np.array([[8,0,0,0,0,0,0,0,0],[0,0,3,6,0,0,0,0,0],[0,7,0,0,9,0,2,0,0],[0,5,0,0,0,7,0,0,0],[0,0,0,0,4,5,7,0,0],[0,0,0,1,0,0,0,3,0],[0,0,1,0,0,0,0,6,8],[0,0,8,5,0,0,0,1,0],[0,9,0,0,0,0,4,0,0]])
game.create_blocks(game.board)
output_board, is_solved = game.simple_solve()
output = game.recursive_solve(output_board, 9)
print(output)

# play simple game
game = Game(4)
# game.board = np.array([[1,2,3,4],[3,4,1,2,],[2,3,4,1],[4,1,2,3]])
game.board = np.array([[1,2,3,4],[0,4,0,2,],[2,3,0,1],[0,1,2,3]])
game.create_blocks(game.board)
output = game.simple_solve()
print(output)

# play 9x9 game easy difficulty
game = Game()
game.board = np.array([[0,2,0,4,5,6,7,8,9],[4,5,7,0,8,0,2,3,6],[6,8,9,2,3,7,0,4,0],[0,0,5,3,6,2,9,7,4],[2,7,4,0,9,0,6,5,3],[3,9,6,5,7,4,8,0,0],[0,4,0,6,1,8,3,9,7],[7,6,1,0,4,0,5,2,8],[9,3,8,7,2,5,0,6,0]])
game.create_blocks(game.board)
output = game.simple_solve()
print(output)


# play very hard from book
game = Game()
game.board = np.array([[0,7,0,0,0,0,2,0,0],[4,0,0,0,9,0,0,3,0],[0,0,3,0,0,2,9,0,8],[2,0,0,7,0,8,0,0,0],[0,3,6,5,1,9,8,2,0],[0,0,0,2,0,3,0,0,5],[3,0,9,1,0,0,7,0,0],[0,4,0,0,2,0,0,0,3],[0,0,2,0,0,0,0,6,0]])
game.create_blocks(game.board)
output_board, is_solved = game.simple_solve()
print(output_board, is_solved)
output_board, is_solved = game.recursive_solve(output_board, 9)
print(output_board)

