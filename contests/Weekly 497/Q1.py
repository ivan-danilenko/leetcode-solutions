"""
Q1. Find the Degree of Each Vertex
Event: Weekly Contest 497
Topic: Staff, Weekly Contest 497
Difficulty: Easy
Status: Solved
Date: 2026-04-11
"""


class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        # to avoid copying
        degrees = [0] * len(matrix)

        for i in range(len(matrix)):
            degrees[i] = sum(matrix[i])
        return degrees


def test():
    sol = Solution()

    cases = [
        (
            {"matrix": [[0, 1, 1], [1, 0, 1], [1, 1, 0]]},
            [2, 2, 2],
        ),
        (
            {"matrix": [[0, 1, 0], [1, 0, 0], [0, 0, 0]]},
            [1, 1, 0],
        ),
        (
            {"matrix": [[0]]},
            [0],
        ),
    ]

    for i, (kwargs, expected) in enumerate(cases, 1):
        print(f"running test {i}")
        got = sol.findDegrees(**kwargs)
        assert got == expected, f"case {i} failed: got {got}, expected {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
