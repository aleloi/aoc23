import string
import api

part1 = False
lvl = 1 if part1 else 2

def replace(s: str, ds):
    where, what = 10**10, None
    for x in string.digits:
        if x in s:
            where = min(where, s.index(x))
    for ns in ds:
        if ns in s and s.index(ns) < where:
            where, what = s.index(ns), ns
    if what is not None:
        s = s.replace(what, ds[what])
    return s


nums_s = ["one", "two", "three", "four", "five", "six", "seven", "eight",  "nine"]

res = 0
lines = api.get_data().splitlines()
for l in lines:
    if not part1:
        l = replace(l, {ns: str(n) for (n, ns) in enumerate(nums_s, 1)})
        l = replace(l[::-1], {ns[::-1]: str(n) for (n, ns) in enumerate(nums_s, 1)} )[::-1]
    nums = [x for x in l if x in string.digits]
    res += int(nums[0] + nums[-1])


if input(f"submit ans={res}, lvl={lvl}? y/n> ") != 'n':
    api.submit(res, lvl)
