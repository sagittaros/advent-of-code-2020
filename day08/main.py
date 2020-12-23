from typing import List, Tuple, Optional

Instruction = Tuple[str, int]


def nop(val: int, cursor: int, _: int):
    # print(f"nop -> val({val}) @ {cursor}->{cursor+1}")
    return (val, cursor + 1)


def jmp(val: int, cursor: int, m: int):
    # print(f"jmp({m}) -> val({val}) @ {cursor}->{cursor+m}")
    return (val, cursor + m)


def acc(val: int, cursor: int, m: int):
    # print(f"acc({m}) -> val({val+m}) @ {cursor}->{cursor+1}")
    return (val + m, cursor + 1)


def early_term(ins: List[Instruction]):
    visited = []  # cursor, invariant: never visit twice
    cur = 0
    val = 0
    while cur < len(ins):
        f, m = ins[cur]
        val, cur = globals()[f](val, cur, m)
        if cur in visited:
            # print("cur:", cur)
            return val
        visited = [*visited, cur]


def backtrack(ins: List[Instruction]):
    visited = []  # cursor, invariant: never visit twice
    tried = []  # cursors. subset of visited
    cur = 0
    val = 0
    forked_len = len(ins)
    mut: Optional[Tuple[int, str]] = None  # (cur, fn)
    while cur < len(ins):
        f, m = ins[cur]
        if mut and mut[0] == cur:
            f = mut[1]
            # print(f"* mut: {f}, {cur}")
            mut = None
        val, cur = globals()[f](val, cur, m)
        if cur in visited:
            # begin backtrack
            while True:
                cur = visited.pop()
                f, m = ins[cur]
                val = val - m if f == "acc" else val
                # print(f"pop {f} => val({val}) @ {cur}")
                if (
                    f in ["nop", "jmp"]
                    and cur not in tried
                    and len(visited) < forked_len
                ):
                    f = "nop" if f == "jmp" else "jmp"
                    mut = (cur, f)
                    forked_len = len(visited)
                    tried = [*tried, cur]
                    break
        else:
            # push into stack
            visited = [*visited, cur]
    return val


with open("input.txt") as f:
    ins = [n.split(" ") for n in f.read().split("\n") if n != ""]
    ins = [(i, int(n)) for i, n in ins]

    # part 1
    print("\nearly term: ", early_term(ins))

    # part 2
    print("\nbacktrack: ", backtrack(ins))
