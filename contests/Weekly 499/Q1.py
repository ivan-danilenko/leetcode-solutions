"""
Q1.
Event: Weekly Contest 499
Topic: Staff, Weekly Contest 499
Difficulty: Easy
Status: Solved
Date: 2026-04-25
"""


class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        max_to_the_right = [None] * len(nums)

        max_to_the_right[-1] = nums[-1]
        for i in range(len(nums) - 2, 0, -1):
            max_to_the_right[i] = max(nums[i], max_to_the_right[i + 1])

        result = [nums[0]]
        max_to_the_left = nums[0]
        for i in range(1, len(nums) - 1):
            if nums[i] > max_to_the_left:
                result.append(nums[i])
                max_to_the_left = nums[i]
            elif nums[i] > max_to_the_right[i + 1]:
                result.append(nums[i])

        if len(nums) > 1:
            result.append(nums[-1])

        return result


def test():
    sol = Solution()

    cases = [
        (
            {"nums": [4, 1, 7, 7]},
            [4, 7, 7],
        ),
        (
            {"nums": [1, 2, 4, 2, 3, 2]},
            [1, 2, 4, 3, 2],
        ),
        (
            {"nums": [5, 5, 5, 5]},
            [5, 5],
        ),
        (
            {"nums": [1]},
            [1],
        ),
    ]

    for i, (kwargs, expected) in enumerate(cases, 1):
        print(f"running test {i}")
        got = sol.findValidElements(**kwargs)
        assert got == expected, f"case {i} failed: got {got}, expected {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
