"""
    Sudoku Solver
    This program extracts a sudoku puzzle from a text file, solves the 
    puzzle then outputs the result to a text file.

    How to:
        1.  Enure sudoku_algorithm.py, sudoku_solver.py and the text
            puzzle file are in the same folder.
        2.  Run sudoku_solver.py.
        3.  Enter the name of the text file including the extension.
        4.  Press enter after entering the name.
        5.  Results and feedback are outputted to solved_puzzles.txt
    
    File format:
    -   File must only contain integers 0 to 9
    -   0's represent an empty square
    -   A file can multiple puzzle, separated with a new line
    -   No spaces are required between numbers

    Author: Krisna Gusti
"""

from sudoku_algorithm import validate_puzzle
from sudoku_algorithm import possible_combinations
from sudoku_algorithm import algorithm
from sudoku_algorithm import is_puzzle_complete

def extract_puzzle(str_puzzle):
    """Convert the puzzle string into a 2D integer list"""
    new_puzzle = []
    row = []

    for line in str_puzzle:
        if len(line) > 10:
            return ["A line was found to be greater than 9 integers."] 
        for number in line:
            try:
                if number != "\n":
                    row.append(int(number))
            except ValueError:
                return ["Non integer was found."]
        new_puzzle.append(row)
        row = []
    
    return new_puzzle

def get_puzzles(file_name):
    """Extract all puzzles from a given file into a list of puzzles"""
    puzzles = []
    puzzle = []

    # Open file
    try:
        file = open(file_name, "r")
    except FileNotFoundError:
        print(f"Could not find file {file_name}. Try again.")
        return False

    # Extract puzzle and append to puzzles list
    for line in file:
        if line != "\n":
            puzzle.append(line)
        if len(puzzle) == 9:
            puzzles.append(extract_puzzle(puzzle))
            puzzle = []
        elif line == "\n" and len(puzzle) > 0:
            puzzles.append(["Puzzle incorrect length"])
            puzzle = []
    
    return puzzles

def write_to_file(puzzle):
    """Writes a single puzzle to file"""
    FILE_NAME = "solved_puzzles.txt"
    
    # Open file
    try:
        file = open(FILE_NAME, "a")
    except FileNotFoundError:
        print("Something went wrong when appending the solutions to the file." \
              "Exiting.")
        quit()

    # Append puzzle to file
    if len(puzzle) > 1:
        SIZE = len(puzzle)
        for i in range(SIZE):
            row = ""
            for j in range(SIZE):
                row += (str(puzzle[i][j]))
                if j != SIZE-1: 
                    row += " "
                if j % 3 == 2 and j != SIZE-1:
                    row += "| "
            file.write(row + "\n")
            if i % 3 == 2 and i != SIZE-1:
                file.write("------+-------+------\n")
        file.write("\n")
    
    # Append error if puzzle could not be solved
    elif puzzle != []:
        file.write("Unable to solve puzzle. " + str(puzzle[0]) + "\n")
        file.write("\n")
    
    file.close()


def solve_puzzle(puzzle):
    """Validates and attempts solves a single puzzle."""
    # Error detected 
    if len(puzzle) <= 1:
        return puzzle
    
    # Attempt to solve puzzle
    elif validate_puzzle(puzzle):
        possible_values = {}
        possible_combinations(puzzle, possible_values)
        algorithm(puzzle, possible_values)

        # Ensure solved puzzle is correct
        if is_puzzle_complete(puzzle):
            return puzzle
        else:
            return ["Puzzle has no solution."]

    return ["Invalid puzzle."]

def main():
    """Gets file, extracts and solves puzzles.
       Outputs result to file."""
    # Get file and extract puzzles
    while True:
        FILE_NAME = input("Please enter the file name: ")
        puzzles = get_puzzles(FILE_NAME)
        if puzzles:
            break
    
    # Create blank file
    file = open("solved_puzzles.txt", "w")
    file.close()

    # For each puzzle solve and write to file
    for puzzle in puzzles:
        solved_puzzle = solve_puzzle(puzzle)
        write_to_file(solved_puzzle)

if __name__ == "__main__":
    main()