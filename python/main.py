import battleship

def launchGame():

	open('conf.txt')

	boardRow = ['O' for i in range(nRow)]
	board = [list(boardRow) for i in range(nCol)]

	print("------- BattleShip V0.1 --------")



	print("\n------- adding a hidden ship ----")
	battleship.addHiddenShip(board)
	battleship.printBoard(board)

	
	tries = 3

	while tries >0:
		row = int(input("Ship's row? : "))
		col = int(input("Ship's Col? : "))

		result = battleship.hasShipBeenFound(board, row, col)
		
		if (result):
			break
		tries -=1

	if (tries >0):
		print("Congratulations, you found the ship")
	else:
		print("Sorry, ship not found")


launchGame()