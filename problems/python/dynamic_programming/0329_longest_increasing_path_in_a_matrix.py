"""
329. Longest Increasing Path in a Matrix
Topic: Array, Dynamic Programming, Depth-First Search, Breadth-First Search,
  Graph Theory, Topological Sort, Memoization, Matrix
Difficulty: Hard
Status: Solved
Date: 2026-05-21

Key idea:
- We have an acyclic directed graph: cells are vertices and a wall
  between cells gives an edge going from the lower to the higher height.
  Then use an algorithm to find the longest chain in a DAG.
- Use topological sort: a linear extension of this order. Here we can
  sort by the height.
- Memoize results in a matrix table.
"""

from typing import List
from itertools import product


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        cells = sorted(product(range(n), range(m)), key=lambda x: matrix[x[0]][x[1]])

        results = [[0] * m for _ in range(n)]

        increments = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def max_of_neighbors(i, j):
            result = 0
            for di, dj in increments:
                new_i, new_j = i + di, j + dj
                if new_i < 0 or new_i >= n or new_j < 0 or new_j >= m:
                    continue
                # to ensure strict increasing
                if matrix[i][j] == matrix[new_i][new_j]:
                    continue
                if result < results[new_i][new_j]:
                    result = results[new_i][new_j]

            return result

        max_length = 0
        for i, j in cells:
            results[i][j] = max_of_neighbors(i, j) + 1
            if results[i][j] > max_length:
                max_length = results[i][j]

        return max_length


def test():
    sol = Solution()

    cases = [
        (
            {
                "matrix": [[9, 9, 4], [6, 6, 8], [2, 1, 1]],
            },
            4,
        ),
        (
            {
                "matrix": [[3, 4, 5], [3, 2, 6], [2, 2, 1]],
            },
            4,
        ),
        (
            {
                "matrix": [[1]],
            },
            1,
        ),
    ]

    for i, (kwargs, expected) in enumerate(cases, 1):
        print(f"running test {i}")
        got = sol.longestIncreasingPath(**kwargs)
        assert got == expected, f"case {i} failed: got {got}, expected {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
