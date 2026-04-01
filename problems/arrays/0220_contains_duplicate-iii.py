"""
220. Contains Duplicate III
Topic: Array, Sliding Window, Sorting, Bucket Sort, Ordered Set
Difficulty: Hard
Status: Solved
Date: 2026-03-23

Key idea:
- Sliding window keeps track of last

Mistakes:
- Edge case `indexDiff == nums.length`
"""

from typing import List
from bisect import bisect_left


class Solution:
    def containsNearbyAlmostDuplicate(
        self, nums: List[int], indexDiff: int, valueDiff: int
    ) -> bool:
        window = nums[: indexDiff + 1]
        window.sort()

        for j in range(len(window) - 1):
            if window[j + 1] - window[j] <= valueDiff:
                return True

        for i in range(len(nums) - indexDiff - 1):
            old_position = bisect_left(window, nums[i])
            new_value = nums[i + indexDiff + 1]
            new_position = bisect_left(window, new_value)
            if old_position < new_position:
                window[old_position : new_position - 1] = window[
                    old_position + 1 : new_position
                ]
            elif old_position > new_position:
                window[new_position + 1 : old_position + 1] = window[
                    new_position:old_position
                ]
            if nums[i] < new_value:
                new_position -= 1
            window[new_position] = new_value

            if (
                new_position > 0
                and window[new_position] - window[new_position - 1] <= valueDiff
            ):
                return True
            if (
                new_position < len(window) - 1
                and window[new_position + 1] - window[new_position] <= valueDiff
            ):
                return True

        return False


def test():
    sol = Solution()

    cases = [
        (
            {
                "nums": [1, 2, 3, 1],
                "indexDiff": 3,
                "valueDiff": 0,
            },
            True,
        ),
        (
            {
                "nums": [1, 5, 9, 1, 5, 9],
                "indexDiff": 2,
                "valueDiff": 3,
            },
            False,
        ),
        (
            {
                "nums": [1, 5, 9, 0, 4, 8],
                "indexDiff": 2,
                "valueDiff": 3,
            },
            False,
        ),
        (
            {
                "nums": [0, 1, 2, 3, 0, 2],
                "indexDiff": 3,
                "valueDiff": 0,
            },
            True,
        ),
        (
            {
                "nums": [-3, 3],
                "indexDiff": 2,
                "valueDiff": 4,
            },
            False,
        ),
        (
            {
                "nums": [-2, 3],
                "indexDiff": 2,
                "valueDiff": 5,
            },
            True,
        ),
        (
            {
                "nums": [1, 2, 1, 1],
                "indexDiff": 1,
                "valueDiff": 0,
            },
            True,
        ),
    ]

    for i, (kwargs, expected) in enumerate(cases, 1):
        print(f"running test {i}")
        got = sol.containsNearbyAlmostDuplicate(**kwargs)
        assert got == expected, f"case {i} failed: got {got}, expected {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
