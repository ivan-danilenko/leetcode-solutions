"""
Q3.
Event: Biweekly Contest 182
Topic: Staff, Biweekly Contest 182
Difficulty: Medium
Status: Solved
Date: 2026-05-09
"""

from typing import List


class Solution:
    def minGenerations(self, points: List[List[int]], target: List[int]) -> int:
        tgt = tuple(target)
        next_gen = set(tuple(pt) for pt in points)
        if tgt in next_gen:
            return 0
        pts = set()
        generation = 0

        while next_gen:
            generation += 1
            last_gen = next_gen
            pts.update(last_gen)
            next_gen = set()
            for pt1 in last_gen:
                for pt2 in pts:
                    new_point = tuple((a + b) // 2 for a, b in zip(pt1, pt2))
                    if new_point == tgt:
                        return generation
                    if new_point not in pts:
                        next_gen.add(new_point)

        return -1


def test():
    sol = Solution()

    cases = [
        (
            {
                "points": [[0, 0, 0], [6, 6, 6]],
                "target": [3, 3, 3],
            },
            1,
        ),
        (
            {
                "points": [[0, 0, 0], [5, 5, 5]],
                "target": [1, 1, 1],
            },
            2,
        ),
        (
            {
                "points": [[0, 0, 0], [2, 2, 2], [3, 3, 3]],
                "target": [2, 2, 2],
            },
            0,
        ),
        (
            {
                "points": [[1, 2, 3]],
                "target": [5, 5, 5],
            },
            -1,
        ),
    ]

    for i, (kwargs, expected) in enumerate(cases, 1):
        print(f"running test {i}")
        got = sol.minGenerations(**kwargs)
        assert got == expected, f"case {i} failed: got {got}, expected {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
