import itertools
import collections
import api

part1 = True
sample = False
lvl = 1 if part1 else 2

lines = api.get_data().splitlines()
lines_sample = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
""".strip().split('\n')
if sample:
    lines = lines_sample

def parse():
    for l in lines:
        c, a = l.split()
        yield c, int(a)

CARD_ORDER = "AKQJT98765432"[::-1]

# First nothing, pair, two pair etc
# then c sorted.
def card_key(c: str):
    def type_():
        cc = collections.Counter(c)
        match max(cc.values()):
            case 5: return 5
            case 4: return 4
            case 3:
                if len(cc) == 2: return 3
                else: return 2
            case 2:
                if len(cc) == 3: return 1
                return 0
            case _: return -1
    return type_(), list(map(CARD_ORDER.index, c))

def card_key2(c: str):
    js = [i for i, k in enumerate(c) if k == 'J']
    NO_J = [c for c in CARD_ORDER if c != 'J']
    ncs = []
    for p in itertools.product(NO_J, repeat=len(js)):
        nc = list(c)
        for k, i in zip(p, js):
            nc[i] = k
        ncs.append(''.join(nc))
    best = sorted(ncs, key=card_key)[-1]
    t, _ = card_key(best)

    return t, list(map(lambda k: CARD_ORDER.index(k) if k != 'J' else -1, c))


def solve1():
    ls = list(parse())
    ls = sorted(ls, key = lambda c_a: card_key(c_a[0]))
    res = 0
    for i, (_, a) in enumerate(ls, 1):
        res += i*a
    return res

def solve2():
    ls = list(parse())
    ls = sorted(ls, key = lambda c_a: card_key2(c_a[0]))
    res = 0
    for i, (_, a) in enumerate(ls, 1):
        res += i*a
    return res

res = (solve1 if part1 else solve2)()
print(f"res is : {res}")


if not sample and input(f"submit ans={res}, lvl={lvl}? y/n> ") == 'y':
    api.submit(res, lvl)
