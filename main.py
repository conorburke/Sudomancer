from game.game import Game

game = Game(3)

board = game.board
size = game.size

for i in range(0, size):
    for j in range(0, size - 1):
        pre = (i + j + 1)
        num = pre if pre % size == 0 else pre % size 
        board[i][j] = num

print(board)
print(board.T)

game.solve()

print(board)