from random import randrange 

def printBoard(board):
	for row in board:
		print(row)

def addHiddenShip(board):
	randRow = randrange(0, len(board))
	randCol = randrange(0, len(board[0]))
	
	board[randRow][randCol] = 'X'
	

def hasShipBeenFound(board, row, col):
	# print("len board = "+str(len(board))+" len of col = "+str(len(board[0]))+" row and col = "+str(row)+" "+str(col))
	if not ((0 <= row < len(board)) and (0 <= col < len(board[0]))):
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

def createBoard(nRow, nCol):
	if nRow <= 0:
		return []

	if nCol <=0:
	 	return [[]]

	colRow = ['O'] * nCol
	return [list(colRow) for i in range(nRow)]
