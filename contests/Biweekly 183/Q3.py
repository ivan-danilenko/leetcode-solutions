"""
Q3.
Event: Biweekly Contest 183
Topic: Staff, Biweekly Contest 183
Difficulty: Medium
Status: Solved [bug fixed after the contest]
Date: 2026-05-23

Mistakes:
- The shared set can't be 1x1 on the boundary,
- Mistakes when treating these boundary cases.
"""

from typing import List


class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        def max_horizontal(row, len_at_least_2):
            prev = grid[row][0]
            curr = grid[row][1]
            if len(grid[row]) == 2:
                return prev + curr
            if len_at_least_2:
                best = prev + curr
                curr_sum = max(best, curr)
            else:
                best = max(prev + curr, curr)
                curr_sum = best
            prev = curr
            for i in range(2, len(grid[row])):
                curr = grid[row][i]
                if len_at_least_2 or i == len(grid[row]) - 1:
                    curr_sum = max(curr + prev, curr_sum + curr)
                else:
                    curr_sum = max(curr, curr_sum + curr)
                if curr_sum > best:
                    best = curr_sum

                prev = curr

            return best

        def max_vertical(col, len_at_least_2):
            prev = grid[0][col]
            curr = grid[1][col]
            if len(grid) == 2:
                return prev + curr
            if len_at_least_2:
                best = prev + curr
                curr_sum = max(best, curr)
            else:
                best = max(prev + curr, curr)
                curr_sum = best
            prev = curr
            for i in range(2, len(grid)):
                curr = grid[i][col]
                if len_at_least_2 or i == len(grid) - 1:
                    curr_sum = max(curr + prev, curr_sum + curr)
                else:
                    curr_sum = max(curr, curr_sum + curr)
                if curr_sum > best:
                    best = curr_sum

                prev = curr

            return best

        h_max = max(
            (max_horizontal(i, i == 0 or i == len(grid) - 1) for i in range(len(grid)))
        )
        v_max = max(
            (
                max_vertical(i, i == 0 or i == len(grid[0]) - 1)
                for i in range(len(grid[0]))
            )
        )

        return max(h_max, v_max)


def test():
    sol = Solution()

    cases = [
        (
            {
                "grid": [
                    [13, 14, 12, 7],
                    [-1, -17, 17, 8],
                    [8, -5, 3, 5],
                    [18, -15, 0, 13],
                ]
            },
            46,
        ),
        (
            {
                "grid": [
                    [-5, 5, -5],
                    [-5, -5, -5],
                ]
            },
            0,
        ),
        (
            {
                "grid": [
                    [-2, -3, 2],
                    [-2, 5, -2],
                    [-3, -4, -2],
                ]
            },
            5,
        ),
        (
            {
                "grid": [
                    [-15, -16],
                    [-7, 12],
                ]
            },
            5,
        ),
        (
            {
                "grid": [
                    [1, 2, 0, -3],
                    [1, -2, 1, 0],
                    [-4, 2, -1, 3],
                    [3, -3, 3, -2],
                    [-1, -5, 0, 1],
                ]
            },
            4,
        ),
        (
            {
                "grid": [
                    [4, -2, -3],
                    [-1, -3, -1],
                    [-4, 2, -1],
                ]
            },
            3,
        ),
    ]

    for i, (kwargs, expected) in enumerate(cases, 1):
        print(f"running test {i}")
        got = sol.maxScore(**kwargs)
        assert got == expected, f"case {i} failed: got {got}, expected {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
