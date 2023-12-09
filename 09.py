import numpy as np
import math
import re
import itertools
import api

part1 = False
sample = False
lvl = 1 if part1 else 2

lines = api.get_data().splitlines()
lines_sample = """
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
""".strip().split('\n')
if sample:
    lines = lines_sample

def parse():
    for l in lines:
        yield list(map(int, l.split()))

ls = list(parse())



def solve1():
    res = 0
    for l in ls:
        arrs = [l]
        while not all(x==0 for x in l):
            l = np.diff(l)
            arrs.append(list(l))
        d = 0
        for dl in arrs[::-1]:
            d += dl[-1]
        res += d
    return res


def solve2():
    res = 0
    for l in ls:
        arrs = [l]
        while not all(x==0 for x in l):
            l = np.diff(l)
            arrs.append(list(l))
        d = 0
        for dl in arrs[::-1]:
            d = dl[0] - d
        # for a in arrs: print(a)
        # print(f"Prev: {d}")
        res += d
    return res


res = (solve1 if part1 else solve2)()
print(f"res is : {res}")


if not sample and input(f"submit ans={res}, lvl={lvl}? y/n> ") == 'y':
    api.submit(res, lvl)
