import battleship

boardRow = ['O','O','O','O','O']
board = [list(boardRow),list(boardRow),list(boardRow),list(boardRow),list(boardRow)]

print("------- BattleShip V0.1 --------")

battleship.printBoard(board)

print("\n------- adding a hidden ship ----")
battleship.addHiddenShip(board)