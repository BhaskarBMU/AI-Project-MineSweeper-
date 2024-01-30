from Minesweeper import MinesweeperSolver
from Minesweeper import MINIMIZE, MineSweeper

driver = MinesweeperSolver(dimensions=4, density=0.99, minimize=MINIMIZE.COST, mode=MineSweeper.PRODUCTION)
driver.run()
	