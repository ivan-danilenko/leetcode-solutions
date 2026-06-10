"""
207. Course Schedule
Topic: Depth-First Search, Breadth-First Search, Graph Theory, Topological Sort
Difficulty: Medium
Status: Solved
Date: 2026-06-08

Key idea:
-

"""

from typing import List
from collections import deque, Counter, defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dependencies = defaultdict(set)
        for to_take, req in prerequisites:
            dependencies[req].add(to_take)

        n_prereqs_left = Counter(req for req, _ in prerequisites)
        completable_courses = deque(
            c for c in range(numCourses) if c not in n_prereqs_left
        )

        completed_courses = 0
        while completable_courses:
            completed_courses += 1
            course = completable_courses.pop()
            for c in dependencies[course]:
                n_prereqs_left[c] -= 1
                if n_prereqs_left[c] == 0:
                    completable_courses.append(c)

        return completed_courses == numCourses


def test():
    sol = Solution()

    cases = [
        (
            {
                "numCourses": 2,
                "prerequisites": [[1, 0]],
            },
            True,
        ),
        (
            {
                "numCourses": 2,
                "prerequisites": [[1, 0], [0, 1]],
            },
            False,
        ),
    ]

    for i, (kwargs, expected) in enumerate(cases, 1):
        print(f"running test {i}")
        got = sol.canFinish(**kwargs)
        assert got == expected, f"case {i} failed: got {got}, expected {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
