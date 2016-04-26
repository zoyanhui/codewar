import sys,os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  
sys.path.insert(0,parentdir) 
from testtool.testtool import test


bracket_begin = ["(", "[", "{"]
bracket_end = [")", "]", "}"]
numbers = set(['1','2','3','4','5','6','7','8','9'])

def pop_atoms(atom_stack):
    ret = []
    brackets = []
    while True:
        c = atom_stack.pop()
        if c[0] in bracket_end:
            brackets.append(c[0])
        elif c[0] in bracket_begin:
            brackets.pop()
        else:
            ret.append(c)
        if not brackets:
            break
    return ret

def push_atoms(atom_nums, atom_stack):
    for atom_num in reversed(atom_nums):
        atom_stack.append(atom_num)

def summary(atom_stack):
    ret = {}
    for atom_num in atom_stack:
        if atom_num[0] in bracket_begin or atom_num[0] in bracket_end:
            continue
        cur_total = ret.get(atom_num[0], 0)
        ret[atom_num[0]] = atom_num[1] + cur_total
    return ret

def multiple_atom_nums(atom_stack, cur_num):
    if not cur_num:
        return
    atom_nums = pop_atoms(atom_stack)
    for atom_num in atom_nums:
        atom_num[1] *= int(cur_num)    
    push_atoms(atom_nums, atom_stack) 

def parse_molecule (formula):
    atom_stack = []
    cur_num = ""
    for c in formula:
        if c in numbers:
            cur_num += c
        else:
            multiple_atom_nums(atom_stack, cur_num) 
            cur_num = ""          
            if c >= 'a' and c <= 'z':
                atom_stack[-1][0] = atom_stack[-1][0] + c
            else:
                atom_stack.append([c, 1])
    multiple_atom_nums(atom_stack, cur_num)
    return summary(atom_stack)




def equals_atomically (obj1, obj2):
    if len(obj1) != len(obj2):
        return False
    for k in obj1:
        if obj1[k] != obj2[k]:
            return False
    return True
                

if __name__ == '__main__':
    test.assert_true(equals_atomically(parse_molecule("H2O"), {'H': 2, 'O' : 1}))
    test.assert_true(equals_atomically(parse_molecule("Mg(OH)2"), {'Mg': 1, 'O' : 2, 'H': 2}))
    test.assert_true(equals_atomically(parse_molecule("K4[ON(SO3)2]2"), {'K': 4,  'O': 14,  'N': 2,  'S': 4}))
    test.assert_true(equals_atomically(parse_molecule("(C5H5)Fe(CO)2CH3"), {'H': 8, 'C': 8, 'Fe': 1, 'O': 2}))
    test.assert_true(equals_atomically(parse_molecule("C6H12O6"), {'H': 12, 'C': 6, 'O': 6}))
    

    test.run_test()
