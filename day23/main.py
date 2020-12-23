Input = "158937462"
# Input = "389125467"


def take(cc, cur, n):
    if n == 1:
        return [cc[cur]]
    return [cc[cur]] + take(cc, cc[cur], n - 1)


def find_dest(cc, cur, excl):
    cur -= 1
    if not cur:
        cur = len(cc)
    if cur not in excl:
        return cur
    # find next
    return find_dest(cc, cur, excl)


def move(cc, cur, M):
    for _ in range(M):
        # take 3
        taken = take(cc, cur, 3)
        cc[cur] = cc[taken[-1]]

        # find dest
        dest = find_dest(cc, cur, taken)

        # slot in
        cc[taken[-1]] = cc[dest]
        cc[dest] = taken[0]

        # next
        cur = cc[cur]


def genseq(cc, i=1):
    # omit start
    start = i
    while cc[i] != start:
        i = cc[i]
        yield i


def build_chain(nums):
    return {n: nums[(i + 1) % len(nums)] for i, n in enumerate(nums)}


def part1():
    print("Part1:")
    cups = list(map(int, Input))
    cc = build_chain(cups)
    move(cc, cups[0], 100)
    gen = genseq(cc, 1)
    print(list(gen))


def part2():
    print("Part2:")
    # TODO make lazy
    cups = list(map(int, Input)) + list(range(10, 1_000_000 + 1))
    cc = build_chain(cups)
    move(cc, cups[0], 10_000_000)
    gen = genseq(cc, 1)
    print(next(gen) * next(gen))


part1()
part2()
