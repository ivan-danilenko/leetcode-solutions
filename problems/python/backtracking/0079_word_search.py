"""
79. Word Search
Topic: Array, String, Backtracking, Depth-First Search, Matrix
Difficulty: Medium
Status: Solved
Date: 2026-05-20

Key idea:
- Depth First Search
- Keep track of visited cells

Possible improvements:
- Mark board in-place instead of using a set.
- return "False" early for impossible words (by character count).
"""

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        height = len(board)
        width = len(board[0])
        displacements = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()

        def dfs(r, c, i):
            if board[r][c] != word[i]:
                return False

            if i == len(word) - 1:
                return True

            visited.add((r, c))
            for dr, dc in displacements:
                if r + dr < 0 or r + dr == height:
                    continue
                if c + dc < 0 or c + dc == width:
                    continue
                if (r + dr, c + dc) in visited:
                    continue

                has_word = dfs(r + dr, c + dc, i + 1)
                if has_word:
                    return True
            visited.remove((r, c))

            return False

        for r in range(height):
            for c in range(width):
                has_word = dfs(r, c, 0)
                if has_word:
                    return True

        return False


def test():
    sol = Solution()

    cases = [
        (
            {
                "board": [
                    ["A", "B", "C", "E"],
                    ["S", "F", "C", "S"],
                    ["A", "D", "E", "E"],
                ],
                "word": "ABCCED",
            },
            True,
        ),
        (
            {
                "board": [
                    ["A", "B", "C", "E"],
                    ["S", "F", "C", "S"],
                    ["A", "D", "E", "E"],
                ],
                "word": "SEE",
            },
            True,
        ),
        (
            {
                "board": [
                    ["A", "B", "C", "E"],
                    ["S", "F", "C", "S"],
                    ["A", "D", "E", "E"],
                ],
                "word": "ABCB",
            },
            False,
        ),
    ]

    for i, (kwargs, expected) in enumerate(cases, 1):
        print(f"running test {i}")
        got = sol.exist(**kwargs)
        assert got == expected, f"case {i} failed: got {got}, expected {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
