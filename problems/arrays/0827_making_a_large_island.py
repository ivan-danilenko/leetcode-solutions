"""
827. Making A Large Island
Topic: Principal, Array, Depth-First Search, Breadth-First Search,
  Union-Find, Matrix, Weekly Contest 82
Difficulty: Hard
Status: Solved & Reworked
Date: 2026-03-21

Key idea:
- Every time one encounters an island, DSF to find all pieces of it
  and label every square in the island by a unique identifier, an integer.
- For every identifier remember the size of an island.
- For every sea square find the sum of island around it.
"""

from typing import List
from collections import defaultdict


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # 0 and 1 are already used, we will use colors starting from 2
        # for islands
        current_color = 2
        island_size = defaultdict(int)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid) or grid[r][c] != 1:
                return
            grid[r][c] = current_color
            island_size[current_color] += 1

            for dr, dc in directions:
                dfs(r + dr, c + dc)

        def color_island(r, c):
            nonlocal current_color
            dfs(r, c)
            current_color += 1

        def island_color_and_size(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid) or grid[r][c] == 0:
                return None, 0

            # never computed before
            if grid[r][c] == 1:
                color_island(r, c)

            color = grid[r][c]
            return color, island_size[color]

        largest_island = 0
        for r in range(len(grid)):
            for c in range(len(grid)):
                if grid[r][c] == 0:
                    neighbors_colors_and_sizes = set(
                        island_color_and_size(r + dr, c + dc) for dr, dc in directions
                    )

                    new_island = sum(size for _, size in neighbors_colors_and_sizes) + 1

                    if new_island > largest_island:
                        largest_island = new_island

        if largest_island == 0:
            # only possible if there is no water
            return len(grid) ** 2

        return largest_island


def test():
    sol = Solution()

    cases = [
        (
            {
                "grid": [
                    [1, 0],
                    [0, 1],
                ],
            },
            3,
        ),
        (
            {
                "grid": [
                    [1, 1],
                    [1, 0],
                ]
            },
            4,
        ),
        (
            {
                "grid": [
                    [1, 1],
                    [1, 1],
                ]
            },
            4,
        ),
        (
            {
                "grid": [
                    [0, 0],
                    [0, 0],
                ]
            },
            1,
        ),
        (
            {
                "grid": [
                    [1, 0],
                    [1, 0],
                ]
            },
            3,
        ),
        (
            {
                "grid": [
                    [1, 0, 0, 1, 1],
                    [1, 0, 0, 1, 0],
                    [1, 1, 1, 1, 1],
                    [1, 1, 1, 0, 1],
                    [0, 0, 0, 1, 0],
                ]
            },
            16,
        ),
        (
            {
                "grid": [
                    [1, 0, 0, 0, 1, 0, 1, 0, 1],
                    [0, 1, 0, 0, 1, 0, 0, 0, 0],
                    [1, 0, 1, 0, 1, 1, 0, 0, 0],
                    [1, 1, 1, 1, 1, 0, 0, 0, 0],
                    [1, 1, 0, 1, 0, 1, 1, 1, 0],
                    [0, 0, 0, 1, 0, 1, 0, 1, 1],
                    [1, 1, 1, 1, 0, 0, 1, 1, 0],
                    [0, 1, 1, 1, 0, 1, 0, 0, 1],
                    [1, 1, 1, 0, 1, 0, 1, 0, 1],
                ]
            },
            34,
        ),
    ]

    for i, (kwargs, expected) in enumerate(cases, 1):
        got = sol.largestIsland(**kwargs)
        assert got == expected, f"case {i} failed: got {got}, expected {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
