"""
Q1.
Event: Weekly Contest 500
Topic: Staff, Weekly Contest 500
Difficulty: Easy
Status: Solved
Date: 2026-05-02
"""


class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        result = [0] * len(nums)

        odd_count = 0
        even_count = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] % 2 == 0:
                even_count += 1
                result[i] = odd_count
            else:
                odd_count += 1
                result[i] = even_count

        return result


def test():
    sol = Solution()

    cases = [
        (
            {"nums": [1, 2, 3, 4]},
            [2, 1, 1, 0],
        ),
        (
            {"nums": [1]},
            [0],
        ),
    ]

    for i, (kwargs, expected) in enumerate(cases, 1):
        print(f"running test {i}")
        got = sol.countOppositeParity(**kwargs)
        assert got == expected, f"case {i} failed: got {got}, expected {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
