from random import randrange 

def printBoard(board):
	for row in board:
		print(row)

def addHiddenShip(board):
	randRow = randrange(0, len(board))
	randCol = randrange(0, len(board[0]))
	
	board[randRow][randCol] = 'X'
	

def hasShipBeenFound(board, row, col):
	if (0 > row >= len(board)) or (0 > col >= len(board[0])):
		print("You are out of the ocean !!")
		return False
	elif board[row][col] == 'X':
		print("Yeah, Good job")
		return True
	else:
		board[row][col] = 'M'
		print("Missed")
		printBoard(board)
		return False
