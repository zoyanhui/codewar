import sys,os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  
sys.path.insert(0,parentdir) 
from testtool.testtool import test

remained_ship = [4, 3, 2, 1]

def is_no_ship():
    return 0 == sum(remained_ship)

def next_pos(cur_r, cur_l, row, col, next = 1):
    for _ in range(next):
        if cur_l == col:
            return cur_r, cur_l    
        cur_l += 1
        if cur_l == col and cur_r != row:
            cur_l = 0
            cur_r += 1
    return cur_r, cur_l


def pre_pos(cur_r, cur_l, row, col, pre = 1):
    for _ in range(pre):
        if cur_l == -1:
            return 0, 0
        cur_l -= 1
        if cur_l < 0 and cur_r != 0:
            cur_l = col - 1
            cur_r -= 1
    return cur_r, cur_l


def is_ship(battleField, cur_r, cur_l, row, col, ship_size, hdirection=True):
    for _ in range(ship_size):
        if cur_r == row or cur_l == col or battleField[cur_r][cur_l] == 0:
            return False
        if hdirection:
            cur_l += 1 
        else:
            cur_r += 1
    return True

def remove_ship(battleField, cur_r, cur_l, ship_size, hdirection=True):
    for i in range(ship_size):
        if hdirection:
            battleField[cur_r][cur_l+i] = 0
        else:
            battleField[cur_r+i][cur_l] = 0

def restore_ship(battleField, cur_r, cur_l, ship_size, hdirection=True):
    for i in range(ship_size):
        if hdirection:
            battleField[cur_r][cur_l+i] = 1
        else:
            battleField[cur_r+i][cur_l] = 1



def validate(battleField, cur_r, cur_l, row, col):
    if cur_r == row and is_no_ship():
        return True
    if battleField[cur_r][cur_l] == 0:
        cur_r, cur_l = next_pos(cur_r, cur_l, row, col)
        return validate(battleField, cur_r, cur_l, row, col)
    else:
        for size in range(1, 5):
            if remained_ship[size - 1] == 0:
                continue
            for direction in [True, False]:                
                if is_ship(battleField, cur_r, cur_l, row, col, size, direction):
                    remove_ship(battleField, cur_r, cur_l, size, direction)
                    cur_r, cur_l = next_pos(cur_r, cur_l, row, col)
                    remained_ship[size - 1] -= 1
                    if validate(battleField, cur_r, cur_l, row, col):
                        return True                
                    cur_r, cur_l = pre_pos(cur_r, cur_l, row, col)
                    restore_ship(battleField, cur_r, cur_l, size, direction)
                    remained_ship[size - 1] += 1
        return False

def validateBattlefield(field):
    global remained_ship
    remained_ship = [4, 3, 2, 1]
    if not field:
        return False
    row = len(field)
    col = len(field[0])
    return validate(field, 0, 0, row, col)      


if __name__ == '__main__':
    battleField = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                 [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                 [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]                 
    test.assert_equals(validateBattlefield(battleField), True);

    # concat test case 
    battleField2 = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                 [1, 1, 0, 0, 0, 0, 0, 0, 1, 0],
                 [1, 1, 0, 0, 1, 1, 1, 0, 1, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    test.assert_equals(validateBattlefield(battleField2), True);
    remained_ship = [4, 3, 2, 1]
    battleField3 = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                 [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                 [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    test.assert_equals(validateBattlefield(battleField3), True);

    remained_ship = [4, 3, 2, 1]
    battleField4 = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                 [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                 [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    test.assert_equals(validateBattlefield(battleField4), False);     
    test.run_test()