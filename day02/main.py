from dataclasses import dataclass
from typing import List


@dataclass
class Spec:
    x: int
    y: int
    alphabet: str
    password: str


def valid_passwords_policy_1(specs: List[Spec]):
    length = lambda a, p: len([c for c in p if c == a])
    return sum(
        [
            1
            for s in specs
            if length(s.alphabet, s.password) >= s.x
            and length(s.alphabet, s.password) <= s.y
        ]
    )


def valid_passwords_policy_2(specs: List[Spec]):
    pos_match = lambda a, p, i: p[i - 1] == a
    return sum(
        [
            1
            for s in specs
            if pos_match(s.alphabet, s.password, s.x)
            != pos_match(s.alphabet, s.password, s.y)
        ]
    )


with open("input.txt") as f:
    items = [(*n.split(":"),) for n in f.read().split("\n") if n != ""]
    specs = []

    for a, b in items:
        policy, alphabet = a.split(" ")
        password = b.strip()
        x, y = policy.split("-")
        specs = [*specs, Spec(int(x), int(y), alphabet, password)]

    print(valid_passwords_policy_1(specs))
    print(valid_passwords_policy_2(specs))
