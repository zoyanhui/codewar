import sys,os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  
sys.path.insert(0,parentdir) 
from testtool.testtool import test


def solve(mmap, miner, exit):
    visited = [[False] * len(mmap[0]) for _ in range(len(mmap))]
    paths = []
    if find_path(mmap, visited, miner, exit, paths):
        return paths
    else:
        return []

def find_path(mmap, vmap, now, exit, paths):
    if now == exit:
        return True
    vmap[now['x']][now['y']] = True
    if now['x'] > 0 and mmap[now['x'] - 1][now['y']] and (not vmap[now['x'] - 1][now['y']]):
        paths.append('left')
        if find_path(mmap, vmap, {'x':now['x'] - 1, 'y': now['y']}, exit, paths):
            return True
        paths.pop()
    if now['y'] > 0 and mmap[now['x']][now['y'] - 1] and (not vmap[now['x']][now['y'] - 1]):
        paths.append('up')
        if find_path(mmap, vmap, {'x':now['x'], 'y': now['y'] - 1}, exit, paths):
            return True
        paths.pop()
    if now['x'] < len(mmap) - 1 and mmap[now['x'] + 1][now['y']] and (not vmap[now['x'] + 1][now['y']]):        
        paths.append('right')        
        if find_path(mmap, vmap, {'x':now['x'] + 1, 'y': now['y']}, exit, paths):
            return True
        paths.pop()
    if now['y'] < len(mmap[0]) - 1 and mmap[now['x']][now['y'] + 1] and (not vmap[now['x']][now['y'] + 1]):
        paths.append('down')
        if find_path(mmap, vmap, {'x':now['x'], 'y': now['y'] + 1}, exit, paths):
            return True
        paths.pop()
    return False


if __name__ == '__main__':
    minemap = [[True]]    
    test.assert_equals(solve(minemap, {'x':0,'y':0}, {'x':0,'y':0}), [])

    minemap = [[True, False],
        [True, True]]
       
    test.assert_equals(solve(minemap, {'x':0,'y':0}, {'x':1,'y':0}), ['right'])
   
    test.assert_equals(solve(minemap, {'x':0,'y':0}, {'x':1,'y':1}), ['right', 'down'])
    
    minemap = [[True], [True], [True], [True]]
          
    test.assert_equals(solve(minemap, {'x':0,'y':0}, {'x':3,'y':0}), ['right', 'right', 'right'])
      
    test.assert_equals(solve(minemap, {'x':3,'y':0}, {'x':0,'y':0}), ['left', 'left', 'left'])

    minemap = [[True, True, True],
      [False, False, True],
      [True, True, True]]
    test.assert_equals(solve(minemap, {'x':0,'y':0}, {'x':2,'y':0}), ['down', 'down', 'right', 'right', 'up', 'up'])

    test.run_test()


