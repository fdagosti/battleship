from random import randrange 

def printBoard(board):
	for row in board:
		print(row)

def addHiddenShip(board):
	randRow = randrange(0, len(board))
	randCol = randrange(0, len(board[0]))

	board[randRow][randCol] = 'X'
	print(randRow,randCol)
	printBoard(board)