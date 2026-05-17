"""
Q2.
Event: Weekly Contest 498
Topic: Staff, Weekly Contest 498
Difficulty: Medium
Status: Solved
Date: 2026-04-18
"""


class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        mins = [0] * len(nums)
        mins[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            mins[i] = min(mins[i + 1], nums[i])

        max = nums[0]
        for i in range(len(nums) - 1):
            if max - mins[i] <= k:
                return i

            print(">>", i, max, mins[i])
            if nums[i + 1] > max:
                max = nums[i + 1]

        print(">>", len(nums) - 1, max, mins[-1])
        if max - mins[-1] <= k:
            return len(nums) - 1

        return -1


def test():
    sol = Solution()

    cases = [
        (
            {"nums": [6, 3, 2, 0, 4, 10, 5], "k": 1},
            -1,
        ),
        (
            {"nums": [5, 0, 1, 4], "k": 3},
            3,
        ),
        (
            {"nums": [3, 2, 1], "k": 1},
            -1,
        ),
        (
            {"nums": [0], "k": 0},
            0,
        ),
    ]

    for i, (kwargs, expected) in enumerate(cases, 1):
        print(f"running test {i}")
        got = sol.firstStableIndex(**kwargs)
        assert got == expected, f"case {i} failed: got {got}, expected {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
