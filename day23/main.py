Input = "389125467"
# Input = "158937462"
Moves = 10


def circular_slice(ls, start, L):
    mod = lambda n: n % (len(ls))
    s = mod(start)
    e = mod(start + L)
    if s < e:
        return ls[s:e]
    else:
        return ls[s:] + ls[0:e]


def without(ls, ss):
    return [c for c in ls if c not in ss]


def pick3(ls, i):
    return circular_slice(ls, i + 1, 3)


def find_next_lower(ls, than):
    if than == 0:
        return max(ls)
    if than - 1 in ls:
        return than - 1
    return find_next_lower(ls, than - 1)


if __name__ == "__main__":
    print("Input: ", Input)
    print("===============")

    cups = list(map(int, [*Input]))
    for i in range(Moves):
        print(f"move {i+1}:")
        print("cups: ", cups)
        picked = pick3(cups, i)
        tmp = without(cups, picked)
        dest = tmp.index(find_next_lower(tmp, tmp[i % len(tmp)]))
        cups = tmp[0 : dest + 1] + picked + tmp[dest + 1 :]
        print("picked: ", picked)
        print("dest: ", f"{tmp[dest]} @ index {dest}")
        print()
