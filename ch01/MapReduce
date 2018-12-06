from functools import reduce


def fn(x, y):
    return x * 10 + y


def fn2(s):
    return Digits[s]


def silme_map_reduce(s):
    return reduce(lambda x, y: x * 10 + y, map(fn2, s))


Digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
a = reduce(fn, map(fn2, '13578'))
print(a)
b = silme_map_reduce('3232')
print(b)
