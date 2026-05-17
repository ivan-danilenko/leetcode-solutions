"""
Q1.
Event: Biweekly Contest 181
Topic: Staff, ??
Difficulty: Easy
Status: Solved
Date: 2026-04-25
"""


class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        n_str = f"{n}"
        x_char = f"{x}"

        if n_str[0] == x_char:
            return False

        return x_char in n_str


def test():
    sol = Solution()

    cases = [
        (
            {"n": 101, "x": 0},
            True,
        ),
        (
            {"n": 232, "x": 2},
            False,
        ),
        (
            {"n": 5, "x": 1},
            False,
        ),
    ]

    for i, (kwargs, expected) in enumerate(cases, 1):
        print(f"running test {i}")
        got = sol.validDigit(**kwargs)
        assert got == expected, f"case {i} failed: got {got}, expected {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
