"""
Q2.
Event: Biweekly Contest 181
Topic: Staff, ??
Difficulty: Medium
Status: Solved
Date: 2026-04-25
"""

from itertools import islice


class Solution:
    def compareBitonicSums(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 2
        while left < right:
            mid = (left + right)//2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid

        max_index = left
        asc_sum = sum(islice(nums, max_index + 1))
        desc_sum = sum(islice(nums, max_index, None))
        if asc_sum > desc_sum:
            return 0
        if asc_sum < desc_sum:
            return 1
        return -1


def test():
    sol = Solution()

    cases = [
        (
            {"nums": [1, 3, 2, 1]},
            1,
        ),
        (
            {"nums": [2, 4, 5, 2]},
            0,
        ),
        (
            {"nums": [1, 2, 4, 3]},
            -1,
        ),
        (
            {
                "nums": [
                    1431715,
                    2743039,
                    140521704,
                    230131128,
                    310457146,
                    461111895,
                    590978670,
                    493997730,
                ]
            },
            0,
        ),
        (
            {"nums": [624808078, 958492885, 742499239]},
            1,
        ),
    ]

    for i, (kwargs, expected) in enumerate(cases, 1):
        print(f"running test {i}")
        got = sol.compareBitonicSums(**kwargs)
        assert got == expected, f"case {i} failed: got {got}, expected {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
