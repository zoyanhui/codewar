def solution(number):
    a = 3; b =5
    s = set()
    n = a
    while n < number:
        s.add(n)
        n += a
    n = b
    while n < number:
        s.add(n)
        n += b
    return sum(s)
        


# the solution below is for the summary value is less than number
def solution_other(number):
    a = 3
    b = 5
    m = 1
    n = 1
    oldsum = 0
    newsum = 0
    while newsum < number:    
        while a * m <= b * n and newsum < number:
            oldsum = newsum
            newsum += a * m            
            m += 1
        if newsum < number:
            oldsum = newsum
            newsum += b * n            
            n += 1
    return oldsum

