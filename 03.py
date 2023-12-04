from collections import defaultdict
import re
import api

part1 = False
lvl = 1 if part1 else 2

lines = api.get_data().splitlines()
# lines = """467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..
# """.strip().split('\n')

breakpoint()
def get(c, r):
    width = len(lines)
    height = len(lines[0])
    if 0 <= c < width and 0 <= r < height:
        return lines[r][c]
    return '.'


# `to` is exclusive
def neighs(fro: int, to: int, line: int) :
    for c in range(fro-1, to+1):
        for r in range(line-1, line+2):
            yield get(c, r)

def neighs2(fro: int, to: int, line: int) :
    for c in range(fro-1, to+1):
        for r in range(line-1, line+2):
            yield get(c, r), (c, r)

def solve1():
    res = 0
    for i, l in enumerate(lines):
        for m in re.finditer(r"\d+", l):
            if not all(x.isdigit() or x == '.' for x in neighs(*m.span(), i)):
                res += int(m.group())
    return res

def solve2():
    res = 0
    gears = defaultdict(list)
    for i, l in enumerate(lines):
        for m in re.finditer(r"\d+", l):
            for x, (c, r) in neighs2(*m.span(), i):
                if x == '*':
                    gears[c, r].append(int(m.group()))

    for ns in gears.values():
        if len(ns) == 2:
            res += ns[0]* ns[1]
    return res

res = (solve1 if part1 else solve2)()

if True or input(f"submit ans={res}, lvl={lvl}? y/n> ") == 'y':
    api.submit(res, lvl)
