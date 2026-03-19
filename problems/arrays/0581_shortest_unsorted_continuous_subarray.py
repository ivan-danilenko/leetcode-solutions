"""
581. Shortest Unsorted Continuous Subarray
Topic: Senior, Array, Two Pointers, Stack, Greedy, Sorting, Monotonic Stack
Difficulty: Medium
Status: Solved
Date: 2026-03-18

Key idea:
- compare to sorted
"""

from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        try:
            left_end = next(i for i in range(len(nums)) if sorted_nums[i] != nums[i])
        except StopIteration:
            # array is sorted
            return 0

        right_end = next(
            i for i in range(len(nums) - 1, -1, -1) if sorted_nums[i] != nums[i]
        )

        return right_end - left_end + 1


def test():
    sol = Solution()

    cases = [
        (
            {"nums": [2, 6, 4, 8, 10, 9, 15]},
            5,
        ),
        (
            {"nums": [1, 2, 3, 4]},
            0,
        ),
        (
            {"nums": [1]},
            0,
        ),
        (
            {"nums": [1, 2, 6, 4, 5]},
            3,
        ),
    ]

    for i, (kwargs, expected) in enumerate(cases, 1):
        got = sol.findUnsortedSubarray(**kwargs)
        assert got == expected, f"case {i} failed: got {got}, expected {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
