"""
Q1.
Event: Weekly Contest 505
Topic: Staff, Weekly Contest 505
Difficulty: Easy
Status: Solved
Date: 2026-06-06
"""


class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        return sum(x for x in range(max(n - k, 0), n + k + 1) if x & n == 0)


def test():
    sol = Solution()

    cases = [
        (
            {"n": 2, "k": 3},
            10,
        ),
        (
            {"n": 5, "k": 1},
            0,
        ),
    ]

    for i, (kwargs, expected) in enumerate(cases, 1):
        print(f"running test {i}")
        got = sol.sumOfGoodIntegers(**kwargs)
        assert got == expected, f"case {i} failed: got {got}, expected {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
