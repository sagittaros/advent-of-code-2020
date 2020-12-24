import re
from collections import Counter

Dirs = {
    # each of the complex number is a unit
    # to go east, initial+1
    # to go north west, initial - 1 + 1j
    "e": 1,
    "w": -1,
    "ne": 0 + 1j,
    "nw": -1 + 1j,
    "se": 1 - 1j,
    "sw": 0 - 1j,
}

# hexagon travel rules
assert Dirs["ne"] + Dirs["se"] + Dirs["w"] == 0
assert Dirs["nw"] + Dirs["sw"] + Dirs["e"] == 0


def parse(l):
    return re.compile(r"[ns]?[ew]").findall(l)


def adjacent(loc):
    return [loc + d for d in Dirs.values()]


# TODO SUPER SLOW
def simul_flipx(blacks):
    marked_as_white = [
        b
        for b in blacks
        if len(set(adjacent(b)).intersection(blacks)) == 0
        or len(set(adjacent(b)).intersection(blacks)) > 2
    ]

    # count overlapped white tiles neighboars of blacks
    overlapped_whites = Counter(
        [a for b in blacks for a in adjacent(b) if a not in blacks]
    )
    marked_as_black = [w for w, count in overlapped_whites.items() if count == 2]
    return list(set(blacks).union(set(marked_as_black)) - set(marked_as_white))


def simul_flip(blacks):
    # consider neighbours of blacks in the total set
    # white will be touched by the numbers of black neighbours
    # similarly, black will be touched by the numbers of black neighbours
    # if white is touched exactly 2 times, flip it to black => Count = 2
    # if black is touched by exactly 1 time, DO NOT flip to white => negate(0, >2) => Count = 1
    cs = Counter([a for b in blacks for a in adjacent(b)])
    white_flip_black = lambda c, n: c not in blacks and n == 2
    remained_black = lambda c, n: c in blacks and n == 1
    return [c for c, n in cs.items() if white_flip_black(c, n) or remained_black(c, n)]


with open("input.txt") as f:
    ls = [parse(d) for d in f.read().split("\n") if bool(d)]
    ls = Counter([sum([Dirs[t] for t in tiles]) for tiles in ls])
    blacks = [k for k, v in ls.items() if v % 2]
    print("Part1:")
    print(len(blacks))

    print("Part2:")
    # print(blacks)
    for _ in range(100):
        blacks = simul_flip(blacks)
    print(len(blacks))
