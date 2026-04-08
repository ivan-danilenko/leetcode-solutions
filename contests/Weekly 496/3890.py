"""
3890. Integers With Multiple Sum of Two Cubes
Event: Weekly Contest 496
Topic: Staff, Weekly Contest 496
Difficulty: Medium
Status: Solved
Date: 2026-04-04

Key idea:
- Make a dictionary that counts representations as sum of cubes.
"""

import math
from collections import defaultdict


class Solution:
    def findGoodIntegers(self, n: int) -> list[int]:
        cubes = [x**3 for x in range(math.ceil(math.cbrt(n)))]

        presentation_counter = defaultdict(int)
        for j in range(1, len(cubes)):
            for i in range(j):
                new_sum = cubes[i] + cubes[j]
                if new_sum <= n:
                    presentation_counter[new_sum] += 1
                else:
                    break

        sums_of_cubes = [
            sum_of_cubes
            for sum_of_cubes, presentations in presentation_counter.items()
            if presentations > 1
        ]
        sums_of_cubes.sort()
        return sums_of_cubes


def test():
    sol = Solution()

    cases = [
        (
            {"n": 4104},
            [1729, 4104],
        ),
        (
            {"n": 578},
            [],
        ),
    ]

    for i, (kwargs, expected) in enumerate(cases, 1):
        got = sol.findGoodIntegers(**kwargs)
        assert got == expected, f"case {i} failed: got {got}, expected {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
