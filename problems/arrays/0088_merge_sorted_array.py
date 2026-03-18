"""
88. Merge Sorted Array
Topic: Array, Two Pointers, Sorting
Difficulty: Easy
Status: Solved
Date: 2026-03-17

Key idea:
Start from the end to avoid overwriting the first array

Mistakes:
- Issues with negative indices
- Issue with pasting the remaining of `num2`
"""

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # special case, nothing to sort in
        if n == 0:
            return
        if m == 0:
            nums1[:] = nums2
            return

        # we start from the end of the sorted arrays
        # take into account that last `n`
        # positions of `nums1` are not data
        ind1 = m - 1
        ind2 = n - 1
        for index_result in range(n + m - 1, -1, -1):
            if nums1[ind1] >= nums2[ind2]:
                nums1[index_result] = nums1[ind1]
                ind1 -= 1
                # if no more numbers needed from `num1`
                # then copy the beginning of `num2` to `num1`
                if ind1 < 0:
                    nums1[:index_result] = nums2[: ind2 + 1]
                    break
            else:
                nums1[index_result] = nums2[ind2]
                ind2 -= 1
                # if no more numbers needed from `num2`
                # then the rest of `num1` is correct
                if ind2 < 0:
                    break


def test():
    sol = Solution()

    cases = [
        (
            {"nums1": [1, 2, 3, 0, 0, 0], "m": 3, "nums2": [2, 5, 6], "n": 3},
            [1, 2, 2, 3, 5, 6],
        ),
        (
            {"nums1": [1], "m": 1, "nums2": [], "n": 0},
            [1],
        ),
        (
            {"nums1": [0], "m": 0, "nums2": [1], "n": 1},
            [1],
        ),
        (
            {"nums1": [2, 0], "m": 1, "nums2": [1], "n": 1},
            [1, 2],
        ),
        (
            {"nums1": [0, 0, 0, 0, 0], "m": 0, "nums2": [1, 2, 3, 4, 5], "n": 5},
            [1, 2, 3, 4, 5],
        ),
    ]

    for i, (kwargs, expected) in enumerate(cases, 1):
        sol.merge(**kwargs)
        got = kwargs["nums1"]
        assert got == expected, f"case {i} failed: got {got}, expected {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
