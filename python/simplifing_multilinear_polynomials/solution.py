import re

def parse_monoials_array(monoials_str):
    m = re.search('[+-]{0,1}\d+', monoials_str)
    num = 1
    if m:
        num = int(m.group())
        monoial = monoials_str.split(m.group(), 1)[1]
    elif monoials_str[0] == '+':
        monoial = monoials_str[1:]
    elif monoials_str[0] == '-':
        monoial = monoials_str[1:]
        num = -1
    else:
        monoial = monoials_str
    return (monoial, num)


def split_monomials(poly):
    monoials = re.findall('[+-]{0,1}\d*[a-z]+', poly)
    return [''.join(sorted(m)) for m in monoials if m]


def compare_monoials(monoials_x, monoials_y):
    lenx = len(monoials_x)
    leny = len(monoials_y)
    if lenx > leny:
        return 1
    elif lenx < leny:
        return -1
    else:
        return 1 if monoials_x > monoials_y else -1 if monoials_x < monoials_y else 0


def simplify(poly):
    monoials_tuples = map(parse_monoials_array, split_monomials(monoials))
    print monoials_tuples
    monoials_dict = dict()
    def reduce_monoials_tuples(monoials_x):
        print monoials_x
        coef = monoials_dict.get(monoials_x[0], 0)
        coef += monoials_x[1]
        monoials_dict[monoials_x[0]] =coef        
    map(reduce_monoials_tuples, monoials_tuples)
    sorted_monoials = sorted(list(monoials_dict), cmp = compare_monoials)
    simplified_monoials_arrays = [('+' if monoials_dict[m] > 0 else '-') + ('' if abs(monoials_dict[m]) == 1 else str(abs(monoials_dict[m])) ) + m for m in sorted_monoials if monoials_dict[m] != 0]
    result = ''.join(simplified_monoials_arrays)
    return result if result[0] != '+' else result[1:]

if __name__ == '__main__':
    while True:        
        polymonials = raw_input()
        print simplify(polymonials)

