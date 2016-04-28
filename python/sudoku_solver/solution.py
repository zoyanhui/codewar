import sys,os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  
sys.path.insert(0,parentdir) 
from testtool.testtool import test


def sudoku(puzzle):
    """return the solved puzzle as a 2d array of 9 x 9"""
    if solve(puzzle, 0, 0):
        return puzzle
    return None

def can_set_num(puzzle, i, j, num):
    for n in puzzle[i]:
        if n == num:
            return False
    for r in range(9):
        if puzzle[r][j] == num:
            return False
    box_i = i / 3
    box_j = j / 3
    for r in range(box_i*3, box_i*3 + 3):
        for l in range(box_j*3, box_j*3 + 3):
            if puzzle[r][l] == num:
                return False
    return True


def next_pos(i, j):
    new_j = j + 1
    new_i = i
    if new_j == 9:
        new_i = i + 1
        new_j = 0
    return new_i, new_j

def pre_pos(i, j):
    new_j = j - 1
    new_i = i
    if new_j == -1:
        new_i = i - 1
        new_j = 8
    return new_i, new_j



def solve(puzzle, i, j):
    if i ==9 or j == 9:
        return True
    if i < 0 or j < 0:
        return False
    if puzzle[i][j] == 0:
        for num in range(1, 10):
            if can_set_num(puzzle, i, j, num):
                puzzle[i][j] = num
                i, j = next_pos(i, j)
                if solve(puzzle, i, j):
                    return True
                i, j = pre_pos(i, j)
                puzzle[i][j] = 0
    else:
        i, j = next_pos(i, j)
        if solve(puzzle, i, j):
            return True
        i, j = pre_pos(i, j)
    return False

if __name__ == '__main__':
    puzzle = [[5,3,0,0,7,0,0,0,0],
              [6,0,0,1,9,5,0,0,0],
              [0,9,8,0,0,0,0,6,0],
              [8,0,0,0,6,0,0,0,3],
              [4,0,0,8,0,3,0,0,1],
              [7,0,0,0,2,0,0,0,6],
              [0,6,0,0,0,0,2,8,0],
              [0,0,0,4,1,9,0,0,5],
              [0,0,0,0,8,0,0,7,9]]

    solution = [[5,3,4,6,7,8,9,1,2],
                [6,7,2,1,9,5,3,4,8],
                [1,9,8,3,4,2,5,6,7],
                [8,5,9,7,6,1,4,2,3],
                [4,2,6,8,5,3,7,9,1],
                [7,1,3,9,2,4,8,5,6],
                [9,6,1,5,3,7,2,8,4],
                [2,8,7,4,1,9,6,3,5],
                [3,4,5,2,8,6,1,7,9]]

    test.assert_equals(sudoku(puzzle), solution)
    test.run_test()
