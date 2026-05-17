"""
Q2. Angles of a Triangle
Event: Weekly Contest 497
Topic: Staff, Weekly Contest 497
Difficulty: Medium
Status: Solved
Date: 2026-04-11

Key idea:
- Use the cosine theorem
- Sort sides first: angles automatically sorted, easier checks
- The last angle can be computed by subtracting from 180

Mistakes:
- Output not sorted,
- If using sine therem max angle can have two values.
"""

import math


class Solution:
    def internalAngles(self, sides: list[int]) -> list[float]:
        sides.sort()
        if sides[2] >= sides[0] + sides[1]:
            return []

        cos0 = sides[1]**2 + sides[2]**2 - sides[0]**2
        cos0 /= 2*sides[1]*sides[2]
        cos1 = sides[0]**2 + sides[2]**2 - sides[1]**2
        cos1 /= 2*sides[0]*sides[2]

        angles = [
            math.acos(cos0) / math.pi * 180,
            math.acos(cos1) / math.pi * 180,
            180
        ]
        angles[2] -= angles[0] + angles[1]
        return angles


def test():
    sol = Solution()

    cases = [
        (
            {"sides": [2, 3, 2]},
            [41.40962, 41.40962, 97.18076],
        ),
        (
            {"sides": [3, 4, 5]},
            [36.86990, 53.13010, 90.00000],
        ),
        (
            {"sides": [2, 4, 2]},
            [],
        ),
    ]

    for i, (kwargs, expected) in enumerate(cases, 1):
        print(f"running test {i}")
        got = sol.internalAngles(**kwargs)
        assert got == expected, f"case {i} failed: got {got}, expected {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
