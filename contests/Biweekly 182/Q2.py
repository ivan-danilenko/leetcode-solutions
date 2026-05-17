"""
Q2.
Event: Biweekly Contest 182
Topic: Staff, ??
Difficulty: Medium
Status: Solved
Date: 2026-05-09
"""

from collections import Counter


class Solution:
    def minFlips(self, s: str) -> int:
        if len(s) == 1:
            return 0
        counter = Counter(s)

        all_ones_flips = counter["0"]
        # either zero or one "1" or two "1"s at the ends
        almost_all_zero_flips = max(counter["1"] - 1, 0)
        if s[0] == "1" and s[-1] == "1":
            almost_all_zero_flips -= 1
        return min(all_ones_flips, almost_all_zero_flips)


def test():
    sol = Solution()

    cases = [
        (
            {"s": "1010"},
            1,
        ),
        (
            {"s": "0110"},
            1,
        ),
        (
            {"s": "1000"},
            0,
        ),
        (
            {"s": "1011"},
            1,
        ),
    ]

    for i, (kwargs, expected) in enumerate(cases, 1):
        print(f"running test {i}")
        got = sol.minFlips(**kwargs)
        assert got == expected, f"case {i} failed: got {got}, expected {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
