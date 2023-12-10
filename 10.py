import copy
import collections
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
.....
.S-7.
.|.|.
.L-J.
.....
"""
# lines_sample = """
# ..F7.
# .FJ|.
# SJ.L7
# |F--J
# LJ...
# """
lines_sample = """
7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
"""
lines_sample = """
FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
"""
lines_sample = lines_sample.strip().split('\n')
if sample:
    lines = lines_sample

#######################################
spos = (-1, -1)
adj = collections.defaultdict(set)
UP, RIGHT, DOWN, LEFT = (DIRS := range(4))
DIRS_S = {UP: "UP", RIGHT: "RIGHT", LEFT: "LEFT", DOWN: "DOWN"}

def parse():
    global spos
    def connect(p, d1, d2):
        i, j = p
        go = {LEFT: ((i, j-1), RIGHT),
              RIGHT: ((i, j+1), LEFT),
              DOWN: ((i+1, j), UP),
              UP: ((i-1, j), DOWN)}
        def c(x, y):
            adj[x].add(y)
            adj[y].add(x)
        c((p, d1), (p, d2))
        c((p, d1), go[d1])
        c((p, d2), go[d2])

    for i, l in enumerate(lines):
        for j, c in enumerate(l):
            p = (i, j)
            match c:
                case '.': continue
                case 'S':
                    spos = p
                case '-': connect(p, LEFT, RIGHT)
                case '|': connect(p, UP, DOWN)
                case 'F': connect(p, DOWN, RIGHT)
                case 'J': connect(p, UP, LEFT)
                case 'L': connect(p, UP, RIGHT)
                case '7': connect(p, LEFT, DOWN)

parse()
def walk(pos):
    res = [pos]
    vis = set([pos])
    while True:
        cands = [neigh for neigh in adj[pos] if neigh not in vis]
        match cands:
            case [c]:
                pos = c
                res.append(c)
                vis.add(c)
            case [c, *_]:
                assert False
            case []:
                return res

loop = sorted([walk((spos, dr))  for dr in DIRS], key=len)[-1]


def blow_up(path):
    path.append(path[-1])
    dr_m = {
        LEFT: (0, -1),
        RIGHT: (0, 1),
        UP: (-1, 0),
        DOWN: (1, 0)
    }
    for n1, n2 in zip(path, path[1:]):
        if n1[0] == n2[0]:
            (i, j) = n1[0]
            d1, d2 = n1[-1], n2[-1]

            d1i, d1j = dr_m[d1]
            yield 2*i+d1i, 2*j+d1j

            yield 2*i, 2*j

            d2i, d2j = dr_m[d2]
            yield 2*i+d2i, 2*j+d2j

def blow_up_grid(path):
    b_path = list(blow_up(path))

    grid = [['.']*(2*len(lines[0])) for _ in range(2*len(lines))]
    for a, b in b_path:
        grid[a][b] = '#'
    return grid

grid = blow_up_grid(loop)

def grid_inside2(i, j):
    return -1 <= i < len(grid)+1 and -1 <= j < len(grid[0])+1

def grid_inside(i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])

def grid_get(i, j):
    if grid_inside(i, j):
        return grid[i][j]
    return '.'

def flood_fill(i, j):
    vis = set([(i, j)])
    q = [(i, j)]
    steps = 0
    while q:
        i, j = q.pop()
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            npos = i+di, j+dj
            if npos not in vis and grid_get(*npos) == '.' and grid_inside2(*npos):
                vis.add(npos)
                q.append(npos)
            steps += 1
    return [p for p in vis if grid_inside(*p)]


def solve1():
    coords = set(p  for (p, _) in loop)
    return len(coords) // 2

def plot_blow_up(grid, inside, outside):
    def pl():
        for l in grid:
            print(''.join(l))
        print()
    pl()

    grid = copy.deepcopy(grid)

    for i, j in inside:
        grid[i][j] = 'I'
    pl()


    grid = copy.deepcopy(grid)
    for i, j in outside:
        grid[i][j] = 'O'
    pl()

    for i, l in enumerate(lines):
        for j, c in enumerate(l):
            grid[2*i][2*j] = c
    pl()



def solve2():
    outside = flood_fill(len(grid)-1, len(grid[0])-1)
    inside = None
    for i, l in enumerate(grid):
        for j, c in enumerate(l):
            if (i, j) not in outside and c == '.':
                inside = flood_fill(i, j)
                return len([(i, j) for (i, j) in inside if
                            i%2 == 0 and j%2==0
                            ])
    #plot_blow_up(grid, inside, outside)
    assert inside is not None


res = (solve1 if part1 else solve2)()
print(f"res is : {res}")


if not sample and input(f"submit ans={res}, lvl={lvl}? y/n> ") == 'y':
    api.submit(res, lvl)
