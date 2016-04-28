import sys,os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  
sys.path.insert(0,parentdir) 
from testtool.testtool import test


def sudoku(puzzle):
    """return the solved puzzle as a 2d array of 9 x 9"""
    positions = all_pos(puzzle)
    if solve(puzzle, positions, 0):
        return puzzle
    return None

def combine(list_a, list_b):
    for a in list_a:
        for b in list_b:
            yield a,b

def all_pos(puzzle):
    return [(r,l) for (r,l) in combine(range(9), range(9)) if puzzle[r][l] == 0]    

def possible(puzzle, i, j):
    row_nums = set(puzzle[i])
    col_nums = set([puzzle[r][j] for r in range(9)])  # zip(*puzzle)[j]
    box_i, box_j = i/3, j/3
    box_nums = set([puzzle[r][l] for (r,l) in combine(range(box_i*3, box_i*3+3), range(box_j*3, box_j*3+3))])
    return set(range(1,10)).difference(row_nums.union(col_nums).union(box_nums))


def solve(puzzle, positions, pos):
    if pos == len(positions):
        return True
    i,j = positions[pos]
    for num in possible(puzzle, i, j):
        puzzle[i][j] = num    
        if solve(puzzle, positions, pos + 1):
            return True
        puzzle[i][j] = 0    
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
