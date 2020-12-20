from typing import List, Tuple
import math

SLOPES = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

Coord = Tuple[int, int]
Grid = List[List[int]]


def move(pos: Coord, slope: Coord):
    # right 3, down 1
    x, y = pos
    dx, dy = slope
    return (x + dx, y + dy)


def travel(m: Grid, slope: Coord):
    pos = (0, 0)
    travelled = []
    while pos[1] < len(m):
        xs = m[pos[1]]
        travelled = [*travelled, xs[pos[0] % len(xs)]]
        pos = move(pos, slope)
    return sum(travelled)


def found_trees(m: Grid):
    return [travel(m, s) for s in SLOPES]


with open("input.txt") as f:
    m = [[1 if c == "#" else 0 for c in n] for n in f.read().split("\n") if n != ""]
    # part 1
    print(travel(m, (3, 1)))
    # part 2
    print(math.prod(found_trees(m)))
