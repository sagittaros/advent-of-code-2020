from functools import reduce
from typing import Dict, List, Tuple

from returns.functions import compose
from toolz import take

Color = Tuple[str, str]
Bag = Tuple[int, Color]
BagsDict = Dict[Tuple[str, str], List[Bag]]

ShinyGold = ("shiny", "gold")


def parse(rule: str) -> BagsDict:
    c, cs = rule.split(" contain ")
    c = tuple(take(2, c.split()))
    color_only = lambda s: (int(s[0]) if s[0] != "no" else 0, (s[1], s[2]))
    color_only = compose(str.split, color_only)
    contained = [color_only(b) for b in cs.split(",")]
    contained = [c for c in contained if not c[1] == ("other", "bags.")]
    return {c: contained}


def contains_gold(d, color: Color):
    if ShinyGold in d[color]:
        return True
    else:
        return any([contains_gold(d, v) for v in d[color]])


def valid_bags(bs: BagsDict):
    colors = {c: [x[1] for x in l] for c, l in bs.items()}
    return {" ".join(c) for c in bs.keys() if contains_gold(colors, c)}


def count_bags(bs: BagsDict, color: Color):
    if len(bs[color]):
        return 1 + sum([b[0] * count_bags(bs, b[1]) for b in bs[color]])
    else:
        return 1


with open("input.txt") as f:
    # parse
    bs = [parse(g) for g in f.read().split("\n") if g != ""]
    bs = reduce(lambda ds, d: {**ds, **d}, bs)

    # part 1: find valid bags
    bags = valid_bags(bs)
    [print(b) for b in sorted(bags)]
    print("\nAnswer:", len(bags))

    # part 2: find contained bags
    count = count_bags(bs, ShinyGold) - 1  # -1 because outest is not counted
    print("\nCount:", count)
