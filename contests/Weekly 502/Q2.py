"""
Q2.
Event: Weekly Contest 502
Topic: Staff, Weekly Contest 502
Difficulty: Medium
Status: Solved
Date: 2026-05-16
"""

import math


class Solution:
    def countKthRoots(self, l: int, r: int, k: int) -> int:
        l_root = l ** (1 / k)
        l_root = math.floor(l_root)
        if l_root**k < l:
            l_root += 1
        r_root = r ** (1 / k)
        r_root = math.ceil(r_root)
        if r_root**k > r:
            r_root -= 1

        return r_root - l_root + 1


def test():
    sol = Solution()

    cases = [
        (
            {"l": 1, "r": 9, "k": 3},
            2,
        ),
        (
            {"l": 8, "r": 30, "k": 2},
            3,
        ),
    ]

    for i, (kwargs, expected) in enumerate(cases, 1):
        print(f"running test {i}")
        got = sol.countKthRoots(**kwargs)
        assert got == expected, f"case {i} failed: got {got}, expected {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
