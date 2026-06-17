"""
33. Search in Rotated Sorted Array
Topic: Array, Binary Search
Difficulty: Medium
Status: Solved
Date: 2026-06-17

Key idea:
...
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                # left to `mid` is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # right to `mid` is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


def test():
    sol = Solution()

    cases = [
        (
            {"nums": [4, 5, 6, 7, 0, 1, 2], "target": 0},
            4,
        ),
        (
            {"nums": [4, 5, 6, 7, 0, 1, 2], "target": 3},
            -1,
        ),
        (
            {"nums": [1], "target": 0},
            -1,
        ),
        (
            {"nums": [1], "target": 1},
            0,
        ),
        (
            {"nums": [1, 2], "target": 2},
            1,
        ),
        (
            {"nums": list(range(7)), "target": 3},
            3,
        ),
        (
            {"nums": list(range(7)), "target": 8},
            -1,
        ),
    ]

    for i, (kwargs, expected) in enumerate(cases, 1):
        print(f"running test {i}")
        got = sol.search(**kwargs)
        assert got == expected, f"case {i} failed: got {got}, expected {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
