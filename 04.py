import re
import api

part1 = False
lvl = 1 if part1 else 2

lines = api.get_data().splitlines()
# lines = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
# """.strip().split('\n')

def parse(l):
    card, cont = l.split(": ")
    card_num = int(card.split()[-1])
    have, winning = cont.split(" | ")
    have_ns = list(map(int, have.split()))
    winning_ns = list(map(int, winning.split()))

    return card_num, have_ns, winning_ns


def solve1():
    res = 0
    for line in lines:
        _, h, w = parse(line)
        nw = len([x for x in h if x in w])
        if nw > 0:
            res += 2**(nw-1)
    return res


def solve2():
    d = [1]*len(lines)
    for i, l in enumerate(lines):
        print(f"before card {i+1}, d={d}")
        _, h, w = parse(l)
        nw = len([x for x in h if x in w])
        for j in range(i+1, i+nw+1):
            d[j] += d[i]
    return sum(d)

res = (solve1 if part1 else solve2)()

if input(f"submit ans={res}, lvl={lvl}? y/n> ") == 'y':
    api.submit(res, lvl)
