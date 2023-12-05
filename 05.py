import itertools
import collections
import typing
import re
import api

part1 = True
lvl = 1 if part1 else 2

lines = api.get_data().splitlines()
lines = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
""".strip().split('\n')

class Map(typing.NamedTuple):
    fro: str
    to: str
    mapping: typing.Callable

def parse():
    seeds = lines[0].split("seeds: ")[-1]
    seeds_l = list(map(int, seeds.split()))

    curr_map = []
    map_kind = None, None
    res = []
    def handle_curr_map():
        fr, to = map_kind
        d = {}
        for dest_st, source_st, range_ln in curr_map:
            for dst, src in itertools.islice(zip(itertools.count(dest_st), itertools.count(source_st)), range_ln):
                d[src] = dst
        res.append(Map(fr, to, lambda src: d.get(src, src)))

    for line in lines[1:]:
        if line.endswith("map:"):
            if map_kind != (None, None):
                handle_curr_map()

            what_map, _ = line.split()
            what1, what2 = what_map.split("-to-")
            curr_map = []
            map_kind = (what1, what2)
        elif line:
            a, b, c = list(map(int, line.split()))
            curr_map.append((a, b, c))
    handle_curr_map()

    return seeds_l, res


def solve1():
    s, r = parse()


def solve2():
    pass
    return sum(d)

res = (solve1 if part1 else solve2)()

if input(f"submit ans={res}, lvl={lvl}? y/n> ") == 'y':
    api.submit(res, lvl)
