"""
857. Minimum Cost to Hire K Workers
Topic: Principal, Array, Greedy, Sorting, Heap (Priority Queue), Weekly Contest 90
Difficulty: Hard
Status: Solved
Date: 2026-05-21

Key idea:
- The cost of a group of workers is determined by the largest wage/quality ratio
  and the sum of quality.
- Sort workers by wage/quality ratio.
- Iterate keeping track of all minimal sums of quality for `k-1` workers.

Mistakes:
- `k = 1` case is special (in the old version).
- Not using heap to keep track of lowest quality for `k-1` workers
"""

from typing import List
import heapq


class Solution:
    def mincostToHireWorkers(
        self, quality: List[int], wage: List[int], k: int
    ) -> float:
        if k == 1:
            return min(wage)

        min_quality_heap = []
        min_quality = 0

        workers = sorted(range(len(quality)), key=lambda x: wage[x] / quality[x])

        min_cost = float("inf")
        for i, w in enumerate(workers):
            if len(min_quality_heap) == k - 1:
                possible_min_cost = min_quality * (wage[w] / quality[w]) + wage[w]
                if min_cost > possible_min_cost:
                    min_cost = possible_min_cost

                removed = heapq.heappushpop_max(min_quality_heap, quality[w])
                min_quality += quality[w] - removed
            else:
                heapq.heappush_max(min_quality_heap, quality[w])
                min_quality += quality[w]

        return min_cost


def test():
    sol = Solution()

    cases = [
        (
            {
                "quality": [10, 20, 5],
                "wage": [70, 50, 30],
                "k": 2,
            },
            105.00000,
        ),
        (
            {
                "quality": [3, 1, 10, 10, 1],
                "wage": [4, 8, 2, 2, 7],
                "k": 3,
            },
            30.66667,
        ),
        (
            {
                "quality": [3, 1, 10, 10, 1],
                "wage": [14],
                "k": 1,
            },
            14,
        ),
    ]

    for i, (kwargs, expected) in enumerate(cases, 1):
        print(f"running test {i}")
        got = sol.mincostToHireWorkers(**kwargs)
        assert (
            abs(got - expected) < 0.00001
        ), f"case {i} failed: got {got}, expected {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
