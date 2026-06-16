"""
875. Koko Eating Bananas
Topic: Senior Staff, Array, Binary Search, Weekly Contest 94
Difficulty: Medium
Status: Solved
Date: 2026-06-16

Key idea:
- Let `k` be the pace of eating, `n` the number of bananas,
  `h` time available to eat, `X` the sum of bananas in all piles.
  Then `k` is in `[X/h, X/(h-n))`.
- Do a binary search on all integral `k` in this range.
- Special case: if `h = n`, then it's enough for each pile to be consumed
  within an hour, i.e. mis speed is `max(piles)`.
"""

from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)
        n_bananas = sum(piles)
        left = math.ceil(n_bananas / h) - 1
        right = math.ceil(n_bananas / (h - len(piles)))

        while right - left > 1:
            mid = (left + right) // 2
            time_with_mid_pace = sum(math.ceil(p / mid) for p in piles)
            if time_with_mid_pace <= h:
                right = mid
            else:
                left = mid

        return right


def test():
    sol = Solution()

    cases = [
        (
            {"piles": [3, 6, 7, 11], "h": 8},
            4,
        ),
        (
            {"piles": [30, 11, 23, 4, 20], "h": 5},
            30,
        ),
        (
            {"piles": [30, 11, 23, 4, 20], "h": 6},
            23,
        ),
        (
            {"piles": [312884470], "h": 312884469},
            2,
        ),
    ]

    for i, (kwargs, expected) in enumerate(cases, 1):
        print(f"running test {i}")
        got = sol.minEatingSpeed(**kwargs)
        assert got == expected, f"case {i} failed: got {got}, expected {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
