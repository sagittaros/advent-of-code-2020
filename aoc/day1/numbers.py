from typing import List


def n_numbers_2020(nums: List[int], N, total=2020):
    """
    O(n^2)
    """
    for n in nums:
        if N == 2:  # 2 is the base case
            if total - n in nums:  # there exists a complement(against total) of n
                return n * (total - n)
        else:
            if product := n_numbers_2020(nums, N - 1, total - n):
                return n * product


with open("input.txt") as f:
    nums = [int(n) for n in f.read().split("\n") if n != ""]
    print(n_numbers_2020(nums, 3))
