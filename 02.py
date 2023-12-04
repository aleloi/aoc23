import itertools
import string
import api
import copy

part1 = False
lvl = 1 if part1 else 2

# 12 red cubes, 13 green cubes, and 14 blue cubes
num_d = {"red": 12, "green": 13, "blue": 14}

def parse(l):
    _, l = l.split(": ")
    subs = l.split("; ")
    subs = [x.split(", ") for x in subs]
    for sub in subs:
        for i, num_col in enumerate(sub):
            num, col = num_col.split()
            sub[i] = (int(num), col)
    return subs

s = 0
lines = api.get_data().splitlines()
# lines = """
# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
# """.strip().split('\n')


for g, l in enumerate(lines, 1):
    pl = parse(l)
    if part1:
        pl1 = list(
            itertools.chain.from_iterable(pl))
        for n, c in pl1:
            if num_d[c] < n:
                print(f"Game {g} impossible!")
                break
        else:
            s += g
    else:
        games = [{col: n for (n, col) in game}
                 for game in pl
                 ]
        d = {} #num_d.copy()
        
        for g in games:
            for col, n in g.items():
                d[col] = max(d.get(col, 0), n)
        pw = 1
        for _, n in d.items():
            pw *= n
        print(pw)
        s += pw
res = s

if input(f"submit ans={res}, lvl={lvl}? y/n> ") == 'y':
    api.submit(res, lvl)
