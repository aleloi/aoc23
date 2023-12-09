import math
import re
import itertools
import api

part1 = False
sample = False
lvl = 1 if part1 else 2

lines = api.get_data(day=8).splitlines()
lines_sample = """
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
""".strip().split('\n')
if sample:
    lines = lines_sample

def parse():
    dirs = lines[0]
    assert all(x in 'LR' for x in dirs)

    # AAA = (BBB, BBB) --> [AAA, (BBB, BBB)]
    eqs = []
    for l in lines[2:]:
        gs = re.match(r"(\w+) = \((\w+), (\w+)\)", l)
        assert gs is not None
        eqs.append((gs.group(1), (gs.group(2), gs.group(3))))
    return dirs, eqs

dirs, eqs = parse()
eqs_d = dict(eqs)


def steps(fr, to_p):
    dirs_i = itertools.cycle(dirs)
    n = 0
    while not to_p(fr):
        dr = next(dirs_i)
        fr = eqs_d[fr][0 if dr == 'L' else 1]
        n += 1
    return n

def solve1():
    return steps('AAA', lambda pos: pos == 'ZZZ')


def solve2():
    starts = [x for x in eqs_d if x.endswith('A')]
    dists = [steps(x, lambda pos: pos.endswith('Z')) for x in starts]
    return math.lcm(*dists)

res = (solve1 if part1 else solve2)()
print(f"res is : {res}")


if not sample and input(f"submit ans={res}, lvl={lvl}? y/n> ") == 'y':
    api.submit(res, lvl)
