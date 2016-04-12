def unique_in_order(iterable):
    return reduce(lambda x,y: x+[y] if not x or x[-1]!=y else x, iterable, [])