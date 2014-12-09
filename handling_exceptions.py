__author__ = 'adm'


import math

addresses = ['Pushkinskaya 55 6', 'Fermskoe 36 85', 'Nevskiy 58 8', 'Moskovskiy 7 9', 'Moskovskiy 7']


try:
    m = map(lambda s : int(s.split()[2]), addresses)
    for it in m:
        print(it)
except IndexError as err:
    print("Input string has wrong format. expected error:", err)
b = sorted(addresses, key = len)
print(b)


def squareRoot(x):
    if(x< 0):
        raise Exception('argumentException', 'x should be greater or equal to zero', x)
    return math.sqrt(x)

try:
    squareRoot(-1)
except Exception as err:
    print(err.args[1])
    raise
