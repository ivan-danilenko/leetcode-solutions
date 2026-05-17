"""
Q3.
Event: Weekly Contest 499
Topic: Staff, Weekly Contest 499
Difficulty: Medium
Status: Solved
Date: 2026-04-25
"""


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        return sum(
            nums[i] - nums[i + 1]
            for i in range(len(nums) - 1)
            if nums[i] - nums[i + 1] > 0
        )


def test():
    sol = Solution()

    cases = [
        (
            {"nums": [3, 3, 2, 1]},
            2,
        ),
        (
            {"nums": [5, 1, 2, 3]},
            4,
        ),
    ]

    for i, (kwargs, expected) in enumerate(cases, 1):
        print(f"running test {i}")
        got = sol.minOperations(**kwargs)
        assert got == expected, f"case {i} failed: got {got}, expected {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
