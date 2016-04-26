import sys,os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  
sys.path.insert(0,parentdir) 
from testtool.testtool import test


# directions = { "right": (0, 1), "down": (1, 0), "left" : (0, -1),  "up": (-1, 0)}
directions = [(0,1), (1,0), (0, -1), (-1,0)]

def need_change_direction(i, j, spiral, size, direction):
    if i < 0 or j < 0 or i == size or j == size:
        return True
    d = directions[direction]
    if i + d[0] < size and i + d[0] >=0 and j + d[1] < size and j + d[1] >= 0 and spiral[i+d[0]][j+d[1]] == 1:
        return True
    return False


def spiralize(size):
    if size == 0:
        return []
    spiral = [[0 for _ in range(size)  ] for _ in range(size)]
    direction = 0
    i = 0; j = 0
    old_i, old_j = i, j
    spiral[old_i][old_j] = 1
    i,j = 0,1
    while i >=0 and i < size and j >= 0 and j < size and spiral[i][j] == 0:   
        spiral[old_i][old_j] = 1
        new_i = directions[direction][0] + i
        new_j = directions[direction][1] + j 
        if need_change_direction(new_i,new_j,spiral,size,direction):
            direction = (direction + 1) % 4
            new_i = directions[direction][0] + i
            new_j = directions[direction][1] + j    
        old_i, old_j = i, j
        i, j = new_i, new_j
    return spiral




if __name__ == '__main__':
    test.assert_equals(spiralize(0), [])
    test.assert_equals(spiralize(1), [[1]])
    test.assert_equals(spiralize(2), [[1,1],
                                      [0,1]])
    test.assert_equals(spiralize(3), [[1,1,1],
                                      [0,0,1],
                                      [1,1,1]])
    test.assert_equals(spiralize(5), [[1,1,1,1,1],
                                      [0,0,0,0,1],
                                      [1,1,1,0,1],
                                      [1,0,0,0,1],
                                      [1,1,1,1,1]])
    test.assert_equals(spiralize(8), [[1,1,1,1,1,1,1,1],
                                      [0,0,0,0,0,0,0,1],
                                      [1,1,1,1,1,1,0,1],
                                      [1,0,0,0,0,1,0,1],
                                      [1,0,1,0,0,1,0,1],
                                      [1,0,1,1,1,1,0,1],
                                      [1,0,0,0,0,0,0,1],
                                      [1,1,1,1,1,1,1,1]])
    test.run_test()