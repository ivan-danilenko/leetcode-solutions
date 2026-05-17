"""
Q3.
Event: Weekly Contest 498
Topic: Staff, Weekly Contest 498
Difficulty: Medium
Status: Solved
Date: 2026-04-18


Mistakes:
- Initial configuration may be recolored. Color first, then plan the next step.
"""


class Solution:
    def colorGrid(self, n: int, m: int, sources: list[list[int]]) -> list[list[int]]:
        colored_cells = 0
        result = [[0] * m for i in range(n)]

        to_color = {(r, c): color for r, c, color in sources}
        new_to_color = {}
        increments = [
            [1, 0],
            [0, 1],
            [-1, 0],
            [0, -1],
        ]

        while colored_cells < n * m:
            for (r, c), color in to_color.items():
                if color > result[r][c]:
                    colored_cells += 1
                    result[r][c] = color

            for (r, c), color in to_color.items():
                for inc in increments:
                    new_cell = (r + inc[0], c + inc[1])
                    if (
                        new_cell[0] >= 0
                        and new_cell[0] < n
                        and new_cell[1] >= 0
                        and new_cell[1] < m
                    ):
                        if new_cell in new_to_color:
                            if color > new_to_color[new_cell]:
                                new_to_color[new_cell] = color
                        elif result[new_cell[0]][new_cell[1]] == 0:
                            new_to_color[new_cell] = color

            to_color = new_to_color
            new_to_color = {}

        return result


def test():
    sol = Solution()

    cases = [
        (
            {"n": 3, "m": 3, "sources": [[0, 0, 1], [2, 2, 2]]},
            [[1, 1, 2], [1, 2, 2], [2, 2, 2]],
        ),
        (
            {"n": 3, "m": 3, "sources": [[0, 1, 3], [1, 1, 5]]},
            [[3, 3, 3], [5, 5, 5], [5, 5, 5]],
        ),
        (
            {"n": 2, "m": 2, "sources": [[1, 1, 5]]},
            [[5, 5], [5, 5]],
        ),
        (
            {"n": 1, "m": 5, "sources": [[0, 0, 5], [0, 3, 4], [0, 2, 1]]},
            [[5, 5, 1, 4, 4]],
        ),
    ]

    for i, (kwargs, expected) in enumerate(cases, 1):
        print(f"running test {i}")
        got = sol.colorGrid(**kwargs)
        assert got == expected, f"case {i} failed: got {got}, expected {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
