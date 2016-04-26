import sys,os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  
sys.path.insert(0,parentdir) 
from testtool.testtool import test

import math

def fib_simple(n):
    """Calculates the nth Fibonacci number, simplest"""
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n >= 2:
        return fib_simple(n-1) + fib_simple(n-2)
    if n < 0:
        return fib_simple(n+2) - fib_simple(n+1)

def fib_ex(n):
    """Calculates the nth Fibonacci number, simplest"""
    if n == 0:
        return 0
    if n < 0:
        temp = fib_ex(-n)
        return temp if n &0x1 else -temp
    if n == 1:
        return 1
    return fib_ex(n - 2) + fib_ex(n-1)

def fib_ex2(n):
    """Calculates the nth Fibonacci number with a dict"""
    m_dict = {0:0, 1:1}
    for i in range(2, n+1):
        m_dict[i] = m_dict[i-2] + m_dict[i-1]
    if n < 0:
        temp = m_dict[-n]
        return temp if n &0x1 else -temp
    else:
        return m_dict[n]

def fib_ex3(n):
    """Calculates the nth Fibonacci number by loop iterator"""
    if n < 0:
        temp = fib_ex3(-n)
        return temp if n &0x1 else -temp
    if n in [0,1]:
        return n
    m1 = 0
    m2 =1
    for i in range(2, n+1):
        temp = m1+m2
        temp1 = m1
        m1 = m2
        m2 = temp
    return m2  


# not work right by this method
def do_fib_by_math(n):
    """Calculates the nth Fibonacci number by math formula"""
    fai = (1.0 + math.sqrt(5)) / 2.0
    fain = pow(fai, n)
    # rev_fain = 1.0/fain * pow(-1, n&0x1)
    # ret = (fain - rev_fain) / math.sqrt(5)
    return int(fain / math.sqrt(5))

# calc fibonacci by matrix exponentiation for n >= 2
def do_fib_by_matrix(n):
    A = [[1, 1], [1, 0]]
    matrix_expo = calc_matrix_expo(A, n-1)
    return matrix_expo[0][0]

def matrix_mul(A, B):
    return [[ A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1] ],
    [ A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1] ] ]

def calc_matrix_expo(A, n):
    if n == 1:
        return A
    B = calc_matrix_expo(A, n /2)
    B = matrix_mul(B, B)
    if n & 0x1:
        B = matrix_mul(B, A)
    return B


def fib(n):
    """Calculates the nth Fibonacci number"""
    if n < 0:
        temp = fib(-n)
        return temp if n &0x1 else -temp
    if n in [0,1]:
        return n
    # do fib
    return do_fib_by_matrix(n)


if __name__ == '__main__':
    test.assert_equals(fib(0),0)

    test.assert_equals(fib(1),1)

    test.assert_equals(fib(2),1)

    test.assert_equals(fib(3),2)

    test.assert_equals(fib(4),3)

    test.assert_equals(fib(5),5)

    test.assert_equals(fib(-1),1)

    test.run_test()

    print fib(1500000)