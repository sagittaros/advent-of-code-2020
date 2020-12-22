import os
import re
from math import prod as all_true
from typing import Dict, List

Passport = Dict[str, str]

Policies = {
    "byr": r"^(19[2-9][0-9]|200[012])$",
    "iyr": r"^(201[0-9]|2020)$",
    "eyr": r"^(202[0-9]|2030)$",
    "hgt": r"^(1(9[0-3]|[5-8][0-9])cm|(59|6[0-9]|7[0-6])in)$",
    "hcl": r"^#[0-9a-f]{6}$",
    "ecl": r"^(amb|blu|brn|gry|grn|hzl|oth)$",
    "pid": r"^\d{9}$",
}


def valid_passports_simple(ps: List[Passport]):
    ps = [{f: v for f, v in p.items() if f != "cid"} for p in ps]  # ignore CID
    valid = lambda p: len(p.keys()) == 7
    return len([p for p in ps if valid(p)])


def valid_passports_full(ps: List[Passport]):
    ps = [{f: v for f, v in p.items() if f != "cid"} for p in ps]  # ignore CID
    valid = lambda p: len(p.keys()) == 7 and all_true(
        [bool(re.match(Policies[k], p[k])) for k in p.keys()]
    )
    return len([p for p in ps if valid(p)])


if __name__ == "__main__":
    cwd = os.path.dirname(__file__)
    input_path = os.path.join(cwd, "input.txt")
    with open(input_path) as f:
        ps = [
            ({f.split(":")[0]: f.split(":")[1] for f in n.split()})
            for n in f.read().split("\n\n")
            if n.strip() != ""
        ]
        print(valid_passports_simple(ps))
        print(valid_passports_full(ps))
