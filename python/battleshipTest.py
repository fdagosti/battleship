import battleship
import unittest, math

class battleTest(unittest.TestCase):
	def test_createBoard(self):
		''' testing board creation methods '''

		SIZES_TO_TEST = ((0,0),
			(0,1),
			(1,0),
			(1,1),
			(10,10),
			(10,23),
			(34,2),
			(-1,-1),
			(-1,1),
			(1,-1))

		
		
		for row, col in SIZES_TO_TEST:
			print("testing with "+str(row)+" "+str(col))
			board = battleship.createBoard(row, col)
			
			toTest = row
			if row <=0 :
				toTest = 0
			self.assertEqual(len(board), toTest)

if __name__ == '__main__':
	unittest.main()
