from dataclasses import dataclass
from typing import List


@dataclass
class Space:
    x_lb: int = 0
    x_ub: int = 7
    y_lb: int = 0
    y_ub: int = 127


def seat_id(p: List[str]):
    space = Space()
    bspace = lambda l, u: (u - l + 1) >> 1
    inc_lb = lambda l, u: (l + bspace(l, u), u)
    dec_ub = lambda l, u: (l, u - bspace(l, u))
    for i in p:
        if i == "F":
            l, u = dec_ub(space.y_lb, space.y_ub)
            space.y_lb = l
            space.y_ub = u
        elif i == "B":
            l, u = inc_lb(space.y_lb, space.y_ub)
            space.y_lb = l
            space.y_ub = u
        elif i == "L":
            l, u = dec_ub(space.x_lb, space.x_ub)
            space.x_lb = l
            space.x_ub = u
        elif i == "R":
            l, u = inc_lb(space.x_lb, space.x_ub)
            space.x_lb = l
            space.x_ub = u

    assert space.x_lb == space.x_ub
    assert space.y_lb == space.y_ub
    return space.y_lb * 8 + space.x_lb


def seat_ids(ps: List[List[str]]):
    return [seat_id(p) for p in ps]


def min_max(nums: List[int]):
    bigger_of = lambda a, b: a if a > b else b
    smaller_of = lambda a, b: a if a < b else b
    head, *tail = nums
    mm = (head, head)
    mm2 = min_max(tail) if tail else (head, head)
    return (smaller_of(mm[0], mm2[0]), bigger_of(mm[1], mm2[1]))


with open("input.txt") as f:
    ps = [[*p] for p in f.read().split("\n") if p != ""]
    ids = seat_ids(ps)

    min_id, max_id = min_max(ids)
    print("min: ", min_id)
    print("max: ", max_id)

    # instead of sort+iter O(nlog(n)), we use the inductive law of natural numbers
    sum_of_natural_num = lambda n: n * (n + 1) / 2
    missing_num = int(
        sum_of_natural_num(max_id) - sum_of_natural_num(min_id - 1) - sum(ids)
    )
    print("missing: ", missing_num)
