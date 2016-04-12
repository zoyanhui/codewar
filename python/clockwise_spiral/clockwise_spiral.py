def createSpiral(N):
    # your code here
    if N < 1 or type(N) is not int::
        return []
    curlayer = 0
    cur = 1
    array = []
    for i in range(N):
        array.append(N * [None])
    # array = N * [N * [None]]
    while cur < N * N:        
        goRight(array, curlayer, N - curlayer -1, curlayer, cur)
        cur += N - 2 * curlayer
        goDown(array, curlayer  + 1, N - curlayer - 2, N - 1 - curlayer, cur)    
        cur += N - 2 * curlayer - 2        
        goLeft(array, N - curlayer - 1, curlayer, N - 1 - curlayer, cur)
        cur += N - 2 * curlayer
        goUp(array, N - curlayer - 2, curlayer + 1, curlayer, cur)
        cur += N - 2 * curlayer - 2        
        curlayer += 1
    if cur == N * N:
        array[curlayer][curlayer] = cur
    return array



def goRight(array, start, end, row, num):
    for i in range(start, end + 1):
        array[row][i] = num
        num += 1

def goDown(array, start, end, col, num):
    for i in range(start, end + 1):
        array[i][col] = num 
        num += 1

def goLeft(array, start, end, row, num):
    for i in range(start, end-1, -1):
        array[row][i] = num 
        num += 1

def goUp(array, start, end, col, num):
    for i in range(start, end-1, -1):
        array[i][col] = num 
        num += 1

if __name__ == '__main__':
    print createSpiral(5)

        
