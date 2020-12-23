from functools import partial
from typing import List

# dirty hack, python does not have TCO
import sys

sys.setrecursionlimit(10000)

PREAMBLE = 25

# modified from day1
def n_totallable(nums: List[int], N, total):
    for i, n in enumerate(nums):
        excl = nums[:i] + nums[i + 1 :]
        if N == 2:  # 2 is the base case
            if total - n in excl:  # there exists a complement(against total) of n
                return True
        else:
            if t := n_totallable(excl, N - 1, total - n):
                return t and True


# part 1
def invalid_num_in(nums):
    totallable = partial(n_totallable, N=2)
    for i, n in enumerate(nums[PREAMBLE:]):
        if not totallable(nums[i : i + PREAMBLE], total=n):
            return n
    return -1


def sliding_total(nums, val, s, N, M):
    if s + N >= len(nums):
        return
    if val == M:
        return nums[s : s + N]
    else:
        val = val - nums[s] + nums[s + N]
        return sliding_total(nums, val, s + 1, N, M)


def weakness_block(nums, M):
    for i in range(2, len(nums)):
        if block := sliding_total(nums, sum(nums[0:i]), 0, i, M):
            return block
    return []


with open("input.txt") as f:
    nums = [int(n) for n in f.read().split("\n") if n != ""]

    # part 1
    invalid_num = invalid_num_in(nums)
    print("invalid_num:", invalid_num)

    # part 2
    block = weakness_block(nums, invalid_num)
    print("block:", block)
    print("weakness:", min(block) + max(block))
