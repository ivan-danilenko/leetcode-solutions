"""
Q1.
Event: Biweekly Contest 183
Topic: Staff, ??
Difficulty: Easy
Status: Solved
Date: 2026-05-23
"""


class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        nzeroes = nums.count(0)
        nzeroes_end = nums[-nzeroes:].count(0)

        return nzeroes - nzeroes_end


def test():
    sol = Solution()

    cases = [
        (
            {"nums": [0, 1, 0, 3, 12]},
            2,
        ),
        (
            {"nums": [0, 1, 0, 2]},
            1,
        ),
        (
            {"nums": [0, 0, 0, 3, 12]},
            2,
        ),
    ]

    for i, (kwargs, expected) in enumerate(cases, 1):
        print(f"running test {i}")
        got = sol.minimumSwaps(**kwargs)
        assert got == expected, f"case {i} failed: got {got}, expected {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
