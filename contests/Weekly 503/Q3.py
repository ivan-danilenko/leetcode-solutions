"""
Q3.
Event: Weekly Contest 503
Topic: Staff, Weekly Contest 503
Difficulty: Medium
Status: ?
Date: 2026-05-23

Mistakes:
- Only *left* rotations are allowed
"""

from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        # check if sorted rotated
        drops = 0
        raises = 0
        for i in range(len(nums)):
            if nums[i] < nums[i - 1]:
                drops += 1
            else:
                raises += 1

            if drops > 1 and raises > 1:
                return -1

        min_ind = nums.index(0)
        if min_ind == 0:
            if nums[1] == 1:
                return 0
            else:
                return 2

        # if not reversed
        if nums[min_ind - 1] == len(nums) - 1:
            return min(min_ind, len(nums) - min_ind + 2)
        else:
            rot_number = min(min_ind + 1, len(nums) - min_ind - 1)
            return rot_number + 1


def test():
    sol = Solution()

    cases = [
        (
            {"nums": [0, 2, 1]},
            2,
        ),
        (
            {"nums": [1, 0, 2]},
            2,
        ),
        (
            {"nums": [0, 1, 2]},
            0,
        ),
        (
            {"nums": [1, 2, 0]},
            2,
        ),
        (
            {"nums": [2, 1, 0]},
            1,
        ),
        (
            {"nums": [2, 0, 1]},
            1,
        ),
        (
            {"nums": [0, 1, 3, 2]},
            -1,
        ),
        (
            {"nums": [1, 2, 3, 4, 0]},
            3,
        ),
    ]

    for i, (kwargs, expected) in enumerate(cases, 1):
        print(f"running test {i}")
        got = sol.minOperations(**kwargs)
        assert got == expected, f"case {i} failed: got {got}, expected {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
