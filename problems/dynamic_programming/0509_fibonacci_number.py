"""
509. Fibonacci Number
Topic: Math, Dynamic Programming, Recursion, Memoization
Difficulty: Easy
Status: Solved
Date: 2026-06-08

Key idea:
- Keep track of the last two numbers
"""


class Solution:
    def fib(self, n: int) -> int:
        # F(-1) = 1
        prev_fib, curr_fib = 1, 0
        for _ in range(n):
            curr_fib, prev_fib = curr_fib + prev_fib, curr_fib

        return curr_fib


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
