from returns.functions import compose
from functools import partial


def play(decks):
    p1, p2 = (decks["Player 1"], decks["Player 2"])
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
            return p2
        if len(p2) == 0:
            return p1


def score(deck):
    ln = len(deck)
    return sum([(ln - i) * c for i, c in enumerate(deck)])


with open("input.txt") as f:
    players = [p.split(":") for p in f.read().split("\n\n")]
    parse = compose(partial(filter, bool), partial(map, int))
    decks = {name: list(parse(cards.split("\n"))) for name, cards in players}
    game = play(decks)
    scores = score(game)
    print(game)
    print(scores)
