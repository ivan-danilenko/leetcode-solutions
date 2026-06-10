"""
509. Fibonacci Number
Topic: Math, Dynamic Programming, Recursion, Memoization
Difficulty: Easy
Status: Solved
Date: 2026-06-08

Key idea:
- Keep track of the last two numbers
"""

import math


class Solution:
    def fib(self, n: int) -> int:
        golden_ratio = (1 + math.sqrt(5)) / 2
        golden_ratio_n = golden_ratio**n
        if n % 2 == 0:
            fib = (golden_ratio_n - 1 / golden_ratio_n) / math.sqrt(5)
        else:
            fib = (golden_ratio_n + 1 / golden_ratio_n) / math.sqrt(5)

        return int(fib)


def test():
    sol = Solution()

    cases = [
        ({"n": 2}, 1),
        ({"n": 3}, 2),
        ({"n": 4}, 3),
        ({"n": 30}, 832040),
    ]

    for i, (kwargs, expected) in enumerate(cases, 1):
        print(f"running test {i}")
        got = sol.fib(**kwargs)
        assert got == expected, f"case {i} failed: got {got}, expected {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
