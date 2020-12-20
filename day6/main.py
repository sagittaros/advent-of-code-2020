def any_count(gs):
    return sum([len({*g.replace("\n", "")}) for g in gs])


def every_count(gs):
    counts = []
    for g in gs:
        pn = len(g.split("\n"))
        letters = [*g.replace("\n", "")]
        freq = [letters.count(l) for l in letters]
        pair = dict(zip(letters, freq))
        counts = [*counts, len({l for l, f in pair.items() if f == pn})]
    return sum(counts)


with open("input.txt") as f:
    gs = [g for g in f.read().split("\n\n") if g != ""]
    print(any_count(gs))
    print(every_count(gs))
