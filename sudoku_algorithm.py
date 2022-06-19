"""
    Sudoku Algorithm
    This program can validate (check for any violations), markup (find all 
    possible combinations for each square) and solve sudoku puzzles.
    The algorithm utilises the backtrack algorithm to solve the sudoku puzzle.

    How to:
        1.  Enure sudoku_algorithm.py, sudoku_solver.py and the text
            puzzle file are in the same folder.
        2.  Run sudoku_solver.py.
        3.  Enter the name of the text file including the extension.
        4.  Press enter after entering the name.
        5.  Results and feedback are outputted to solved_puzzles.txt

    Author: Krisna Gusti
"""

def box_range(position):
    """Return box range for a given row or column"""
    if position < 3:
        return [0, 1, 2]
    elif position < 6:
        return [3, 4, 5]
    else:
        return [6, 7, 8]

# Validation - Checks for any violations

def check_row(number, row, solution):
    """Return the number of times a number is seen in a given row"""
    count = 0
    for i in range(len(solution)):
        if solution[row][i] == number:
            count += 1
    return count

def check_col(number, col, solution):
    """Return the number of times a number is seen in a given column"""
    count = 0
    for i in range(len(solution)):
        if solution[i][col] == number:
            count += 1
    return count

def check_box(number, row, col, solution):
    """Return the number of times a number is seen in a given box"""
    count = 0
    for i in box_range(row):
        for j in box_range(col):
            if solution[i][j] == number:
                count += 1
    return count

def validate_puzzle(solution):
    """Check if the puzzle follows the rules"""
    SIZE = len(solution)
    for row in range(SIZE):
        for col in range(SIZE):
            if solution[row][col] != 0:
                count = 0
                count += check_row(solution[row][col], row, solution)
                count += check_col(solution[row][col], col, solution)
                count += check_box(solution[row][col], row, col, solution)
                if count > 3:
                    return False
    return True

def validate_number(number, row, col, solution):
    """Check if a number is valid"""
    count = 0
    count += check_row(number, row, solution)
    count += check_col(number, col, solution)
    count += check_box(number, row, col, solution)
    if count > 0:
        return False
    return True

def is_puzzle_complete(solution):
    """Check all boxes are filled (no 0's)"""
    for i in range(len(solution)):
        for j in range(len(solution)):
            if solution[i][j] == 0:
                return False
    return True

# Markup - Find all possible numbers for each cell

def remove_seen_in_row(row, col, possible_values, solution):
    """Remove seen numbers in row from square in possible values"""
    for i in range(len(solution)):
        if solution[row][i] in possible_values[row, col]:
            possible_values[row, col].remove(solution[row][i])

def remove_seen_in_col(row, col, possible_values, solution):
    """Remove seen numbers in column from square in possible values"""
    for i in range(len(solution)):
        if solution[i][col] in possible_values[row, col]:
            possible_values[row, col].remove(solution[i][col])

def remove_seen_in_box(row, col, possible_values, solution):
    """Remove seen numbers in box from square in possible values"""
    for i in box_range(row):
        for j in box_range(col):
            if solution[i][j] in possible_values[row, col]:
                possible_values[row, col].remove(solution[i][j])

def possible_combinations(solution, possible_values):
    """Find all possible values for each square"""
    SIZE = len(solution)
    for row in range(SIZE):
        for col in range(SIZE):
            if solution[row][col] == 0:
                # start with all possible values
                possible_values[row, col] = list(range(1, SIZE+1))
                # remove values seen
                remove_seen_in_row(row, col, possible_values, solution)
                remove_seen_in_col(row, col, possible_values, solution)
                remove_seen_in_box(row, col, possible_values, solution)
                # If only one possible solution exists, fill in solution
                if len(possible_values[row, col]) == 1:
                    solution[row][col] = possible_values[row, col][0]

# Backtracking Algorithm

def find_empty(solution):
    """Find the next empty box, working left to right, top to bottom"""
    SIZE = len(solution)
    for row in range(SIZE):
        for col in range(SIZE):
            if solution[row][col] == 0:
                return (row, col)
    return False

def algorithm(solution, possible_values):
    """Find a solution utilising the backtrack algorithm """
    next_number = find_empty(solution)
    
    # At the end of the puzzle
    if not next_number:
        return True
    
    row, col = next_number

    # Try all possible values, recursive call if valid otherwise backtrack
    for number in possible_values[row, col]:
        if validate_number(number, row, col, solution):
            solution[row][col] = number
            if algorithm(solution, possible_values):
                return True
            solution[row][col] = 0

    return False