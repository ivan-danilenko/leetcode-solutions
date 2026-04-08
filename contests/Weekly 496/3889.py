"""
3889. Mirror Frequency Distance
Event: Weekly Contest 496
Topic: Staff, Weekly Contest 496
Difficulty: Medium
Status: Solved
Date: 2026-04-04

Key idea:
- Count frequences first, then run over mirror pairs.
"""

import string
from collections import Counter


class Solution:
    def mirrorFrequency(self, s: str) -> int:
        frequencies = Counter(s)

        alphabet = string.ascii_lowercase
        digits = list(range(10))

        freq_sum = sum(
            abs(frequencies[char] - frequencies[char_mirror])
            for char, char_mirror, _ in zip(
                alphabet, alphabet[::-1], range(len(alphabet) // 2)
            )
        )

        freq_sum += sum(
            abs(frequencies[str(dig)] - frequencies[str(dig_mirror)])
            for dig, dig_mirror, _ in zip(digits, digits[::-1], range(len(digits) // 2))
        )

        return freq_sum


def test():
    sol = Solution()

    cases = [
        (
            {"s": "ab1z9"},
            3,
        ),
        (
            {"s": "4m7n"},
            2,
        ),
        (
            {"s": "byby"},
            0,
        ),
    ]

    for i, (kwargs, expected) in enumerate(cases, 1):
        got = sol.mirrorFrequency(**kwargs)
        assert got == expected, f"case {i} failed: got {got}, expected {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
