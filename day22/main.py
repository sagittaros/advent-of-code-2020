from returns.functions import compose
from functools import partial


def play(p1, p2):
    print(p1, p2)
    while True:
        h1, *t1 = p1
        h2, *t2 = p2
        if h1 > h2:
            p1 = [*t1, h1, h2]
            p2 = t2
        else:
            p1 = t1
            p2 = [*t2, h2, h1]
        if len(p1) == 0:
            return (None, p2)
        if len(p2) == 0:
            return (p1, None)


def play_recur(p1, p2, l=1):
    r = 0
    seen = set()
    while True:
        r += 1
        # print(f"Round {r}")

        # check if deck was seen
        state = tuple(p1), tuple(p2)
        if state in seen:
            return (p1, None)
        seen.add(state)

        # each deals a card
        h1, *t1 = p1
        h2, *t2 = p2
        # print("h1,t1:", h1, t1)
        # print("h2,t2:", h2, t2)
        if h1 <= len(t1) and h2 <= len(t2):
            r1, r2 = play_recur(t1[:h1], t2[:h2], l=l + 1)
            if r1:
                p1 = [*t1, h1, h2]
                p2 = t2
            if r2:
                p1 = t1
                p2 = [*t2, h2, h1]
        else:
            if h1 > h2:
                p1 = [*t1, h1, h2]
                p2 = t2
            else:
                p1 = t1
                p2 = [*t2, h2, h1]

        # no more cards
        if len(p1) == 0:
            return (None, p2)
        if len(p2) == 0:
            return (p1, None)


def score(deck):
    if not deck:
        return 0
    ln = len(deck)
    return sum([(ln - i) * c for i, c in enumerate(deck)])


with open("input.txt") as f:
    players = [p.split(":") for p in f.read().split("\n\n")]
    parse = compose(partial(filter, bool), partial(map, int))
    decks = {name: list(parse(cards.split("\n"))) for name, cards in players}

    # part 1
    print("Part 1:")
    p1, p2 = (decks["Player 1"][:], decks["Player 2"][:])
    s1, s2 = play(p1, p2)
    s1, s2 = (score(s1), score(s2))
    print(f"Score: P1={s1}  P2={s2}")

    # part 2
    print("\n\nPart 2:")
    p1, p2 = (decks["Player 1"][:], decks["Player 2"][:])
    s1, s2 = play_recur(p1, p2)
    s1, s2 = (score(s1), score(s2))
    print(f"Score: P1={s1}  P2={s2}")
