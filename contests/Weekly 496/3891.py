"""
3891. Minimum Increase to Maximize Special Indices
Event: Weekly Contest 496
Topic: Staff, Weekly Contest 496
Difficulty: Medium
Status: Solved
Date: 2026-04-04

Key idea:
- maximal number of special indices is `(len(nums) - 1)//2`.
- if `len(nums)` is even, there several potential choices,
  glued from two.
"""

from typing import List


class Solution:
    def minIncrease(self, nums: List[int]) -> int:
        number_of_special_indices = (len(nums) - 1) // 2
        if len(nums) % 2 != 0:
            minimal_steps = 0
            for i in range(number_of_special_indices):
                need_steps = max(nums[2 * i], nums[2 * i + 2]) - nums[2 * i + 1] + 1
                if need_steps > 0:
                    minimal_steps += need_steps

        else:
            # moving from the left end
            left_minimal_steps = [0] * number_of_special_indices
            minimal_steps = 0
            for i in range(number_of_special_indices):
                left_minimal_steps[i] = minimal_steps
                need_steps = max(nums[2 * i], nums[2 * i + 2]) - nums[2 * i + 1] + 1
                if need_steps > 0:
                    minimal_steps += need_steps

            # going from the right end
            right_minimal_steps = 0
            for i in range(number_of_special_indices):
                need_steps = (
                    max(nums[-1 - 2 * i], nums[-1 - 2 * i - 2])
                    - nums[-1 - 2 * i - 1]
                    + 1
                )
                if need_steps > 0:
                    right_minimal_steps += need_steps

                potential_min_steps = right_minimal_steps + left_minimal_steps[-1 - i]
                if potential_min_steps < minimal_steps:
                    minimal_steps = potential_min_steps

        return minimal_steps


def test():
    sol = Solution()

    cases = [
        (
            {"nums": [1, 2, 2]},
            1,
        ),
        (
            {"nums": [2, 1, 1, 3]},
            2,
        ),
        (
            {"nums": [5, 2, 1, 4, 3]},
            4,
        ),
        (
            {"nums": [12, 23, 13, 17, 21, 3]},
            0,
        ),
    ]

    for i, (kwargs, expected) in enumerate(cases, 1):
        print("**********")
        got = sol.minIncrease(**kwargs)
        assert got == expected, f"case {i} failed: got {got}, expected {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
