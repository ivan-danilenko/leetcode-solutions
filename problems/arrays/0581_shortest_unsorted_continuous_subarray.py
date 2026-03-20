"""
581. Shortest Unsorted Continuous Subarray
Topic: Senior, Array, Two Pointers, Stack, Greedy, Sorting, Monotonic Stack
Difficulty: Medium
Status: Solved
Date: 2026-03-19

Key idea:
- Find maximal sorted beginning [greedy approach]. After sorting this beginning
  may not stay the same if further there is an element smaller than any of the
  beginning. We find the min of the rest of the list, and then use `bisect_right`
  to find where it would be sorted into the beginning.
  Repeat the same for the sorted end.
"""

from typing import List
from bisect import bisect_right, bisect_left


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        try:
            max_left_end = next(
                i + 1 for i in range(len(nums) - 1) if nums[i] > nums[i + 1]
            )
        except StopIteration:
            # array is sorted
            return 0

        # we see where the min element of the rest of `nums` would be sorted in
        # keeping as many element of the beginning in place as possible
        min_in_rest = min(nums[max_left_end:])
        left_end = bisect_right(nums, min_in_rest, hi=max_left_end)

        # same for the right end
        min_right_end = next(
            i for i in range(len(nums) - 1, 0, -1) if nums[i - 1] > nums[i]
        )
        max_in_rest = max(nums[:min_right_end])
        right_end = bisect_left(nums, max_in_rest, lo=min_right_end)

        return right_end - left_end


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
        (
            {"nums": [1, 3, 2, 2, 2]},
            4,
        ),
    ]

    for i, (kwargs, expected) in enumerate(cases, 1):
        got = sol.findUnsortedSubarray(**kwargs)
        assert got == expected, f"case {i} failed: got {got}, expected {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
