"""
Q1.
Event: Weekly Contest 502
Topic: Staff, Weekly Contest 502
Difficulty: Easy
Status: Solved
Date: 2026-05-16
"""


class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        return all(abs(int(s[i]) - int(s[i + 1])) <= 2 for i in range(len(s) - 1))


def test():
    sol = Solution()

    cases = [
        (
            {"s": "132"},
            True,
        ),
        (
            {"s": "129"},
            False,
        ),
    ]

    for i, (kwargs, expected) in enumerate(cases, 1):
        print(f"running test {i}")
        got = sol.isAdjacentDiffAtMostTwo(**kwargs)
        assert got == expected, f"case {i} failed: got {got}, expected {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
