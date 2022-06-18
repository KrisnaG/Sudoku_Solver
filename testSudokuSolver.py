import unittest
import sudoku_solver as ss
import sudoku_algorithm as sa


puzzle = [
    [0, 3, 0,   0, 0, 0,    0, 0, 0], 
    [0, 1, 0,   0, 8, 0,    9, 0, 0],
    [2, 0, 0,   0, 0, 0,    0, 0, 0],

    [0, 0, 0,   0, 3, 0,    0, 0, 0],
    [0, 0, 0,   0, 1, 9,    0, 0, 0],
    [0, 0, 0,   2, 0, 8,    0, 0, 0],
    
    [0, 0, 0,   0, 0, 0,    0, 3, 0],
    [0, 9, 0,   8, 0, 0,    0, 1, 0],
    [0, 0, 0,   0, 0, 0,    2, 0, 0]]

solution = [
    [4, 3, 5,   1, 9, 2,    6, 7, 8],
    [6, 1, 7,   3, 8, 4,    9, 2, 5],
    [2, 8, 9,   5, 6, 7,    1, 4, 3],

    [1, 2, 4,   6, 3, 5,    7, 8, 9],
    [3, 5, 8,   7, 1, 9,    4, 6, 2],
    [9, 7, 6,   2, 4, 8,    3, 5, 1],

    [5, 4, 2,   9, 7, 1,    8, 3, 6],
    [7, 9, 3,   8, 2, 6,    5, 1, 4],
    [8, 6, 1,   4, 5, 3,    2, 9, 7]]


class TestSudoku(unittest.TestCase):

    def testStringExtraction(self):
        # Test extraction of a single line
        self.assertEqual(
            ss.extract_puzzle(
                ["012345678","012345678"]), 
            [[0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8]], 
            "Numbers be should be extracted from string into a 2d array")
    
    def testSolution(self):
        # Test ability to solve puzzle and output correct format
        self.assertEqual(
            ss.solve_puzzle(puzzle),
            solution,
            "Should be able to solve puzzle")
    

class TestAlgorithm(unittest.TestCase):
    
    def testBoxRange(self):
        # Test range for a box
        self.assertEqual(
            sa.box_range(3), 
            [3, 4, 5], 
            "Should return an array for 3 numbers")

    def testValidNumber(self):
        # Test if a number can be insert without breaking any rules
        self.assertEqual(
            sa.validate_number(4, 0, 0, puzzle) ,
            True ,
            "Should be able to insert valid number.")
        self.assertEqual(
            sa.validate_number(2, 0, 0, puzzle) ,
            False ,
            "Should not be able to insert number.")
    

if __name__ == "__main__":
    unittest.main()