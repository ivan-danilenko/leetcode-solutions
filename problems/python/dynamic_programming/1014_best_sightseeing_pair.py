"""
1014. Best Sightseeing Pair
Topic: Staff Array Dynamic Programming Weekly Contest 129
Difficulty: Medium
Status: Solved
Date: 2026-03-19

Key idea:
- The score of a pair splits into `values[i] + i` and `values[j] - j` `(i < j)`
- Remember the highest `values[i] + i` so far and the highest pair score.
"""

from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_left_contribution = values[0]
        max_pair_contribution = max_left_contribution + values[1] - 1

        for i in range(1, len(values) - 1):
            new_left_contribution = values[i] + i
            if max_left_contribution < new_left_contribution:
                max_left_contribution = new_left_contribution

            # maximal contribution of pairs with `i + 1` on the right
            new_pair_contribution = max_left_contribution + values[i + 1] - (i + 1)
            if max_pair_contribution < new_pair_contribution:
                max_pair_contribution = new_pair_contribution

        return max_pair_contribution


def test():
    sol = Solution()

    cases = [
        (
            {"values": [8, 1, 5, 2, 6]},
            11,
        ),
        (
            {"values": [1, 2]},
            2,
        ),
    ]

    for i, (kwargs, expected) in enumerate(cases, 1):
        got = sol.maxScoreSightseeingPair(**kwargs)
        assert got == expected, f"case {i} failed: got {got}, expected {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
