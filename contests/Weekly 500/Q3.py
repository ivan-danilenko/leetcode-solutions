"""
Q3.
Event: Weekly Contest 500
Topic: Staff, Weekly Contest 500
Difficulty: Medium
Status: Solved
Date: 2026-05-02
"""


class Solution:
    def minCost(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        cum_costs_to_move_left = [0] * len(nums)
        cum_costs_to_move_right = [0] * len(nums)

        cum_costs_to_move_left[1] = 1
        for i in range(2, len(nums)):
            if nums[i] + nums[i - 2] >= 2 * nums[i - 1]:
                cum_costs_to_move_left[i] = (
                    cum_costs_to_move_left[i - 1] + nums[i] - nums[i - 1]
                )
            else:
                cum_costs_to_move_left[i] = cum_costs_to_move_left[i - 1] + 1

        cum_costs_to_move_right[-2] = 1
        for i in range(len(nums) - 3, -1, -1):
            if nums[i] + nums[i + 2] < 2 * nums[i + 1]:
                cum_costs_to_move_right[i] = (
                    cum_costs_to_move_right[i + 1] + nums[i + 1] - nums[i]
                )
            else:
                cum_costs_to_move_right[i] = cum_costs_to_move_right[i + 1] + 1

        results = [0] * len(queries)
        for i, (l, r) in enumerate(queries):
            if l < r:
                results[i] = cum_costs_to_move_left[r] - cum_costs_to_move_left[l]
            elif l > r:
                results[i] = cum_costs_to_move_right[r] - cum_costs_to_move_right[l]

        return results


def test():
    sol = Solution()

    cases = [
        (
            {"nums": [-5, -2, 3], "queries": [[0, 2], [2, 0], [1, 2]]},
            [6, 2, 5],
        ),
        (
            {"nums": [0, 2, 3, 9], "queries": [[3, 0], [1, 2], [2, 0]]},
            [4, 1, 3],
        ),
        (
            {"nums": [0, 2, 4, 6], "queries": [[3, 0], [0, 3]]},
            [3, 5],
        ),
    ]

    for i, (kwargs, expected) in enumerate(cases, 1):
        print(f"running test {i}")
        got = sol.minCost(**kwargs)
        assert got == expected, f"case {i} failed: got {got}, expected {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
