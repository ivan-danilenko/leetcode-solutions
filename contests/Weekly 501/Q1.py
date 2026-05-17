"""
Q1.
Event: Weekly Contest 501
Topic: Staff, Weekly Contest 501
Difficulty: Easy
Status: Solved
Date: 2026-05-09
"""


class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        return nums + nums[::-1]


def test():
    sol = Solution()

    cases = [
        (
            {"nums": [1, 2, 3]},
            [1, 2, 3, 3, 2, 1],
        ),
        (
            {"nums": [1]},
            [1, 1],
        ),
    ]

    for i, (kwargs, expected) in enumerate(cases, 1):
        print(f"running test {i}")
        got = sol.concatWithReverse(**kwargs)
        assert got == expected, f"case {i} failed: got {got}, expected {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
