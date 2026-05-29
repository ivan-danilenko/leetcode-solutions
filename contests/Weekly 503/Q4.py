"""
Q4.
Event: Weekly Contest 503
Topic: Staff, Weekly Contest 503
Difficulty: Hard
Status: Solved [Removed "Time Exceeded" after the contest]
Date: 2026-05-23

Mistakes:
- Did not optimize for shifts with many elements.
"""

from typing import List
from collections import Counter
from itertools import chain


class Solution:
    def numberOfPairs(
        self, nums1: List[int], nums2: List[int], queries: List[List[int]]
    ) -> List[int]:
        nnums1 = Counter(nums1)
        nnums2 = Counter(nums2)

        result = []

        max_val_nnums1 = max(nnums1.keys())
        max_val_nnums2 = max(nnums2.keys())
        min_val_nnums1 = min(nnums1.keys())
        min_val_nnums2 = min(nnums2.keys())

        overall_shift = 0
        for t, *instr in queries:
            if t == 1:
                x, y, val = instr
                if val == 0:
                    continue
                if 2 * (y - x) > len(nums2):
                    overall_shift += val

                    nnums2_iter = chain(range(x), range(y + 1, len(nums2)))
                    val = -val
                else:
                    nnums2_iter = range(x, y + 1)

                for i in nnums2_iter:
                    nnums2[nums2[i]] -= 1
                    if nnums2[nums2[i]] == 0:
                        del nnums2[nums2[i]]
                    nnums2[nums2[i] + val] += 1
                    nums2[i] += val
                    if nums2[i] > max_val_nnums2:
                        max_val_nnums2 = nums2[i]
                    if nums2[i] < min_val_nnums2:
                        min_val_nnums2 = nums2[i]

            else:
                (tot,) = instr
                tot -= overall_shift
                if max_val_nnums1 + max_val_nnums2 < tot:
                    result.append(0)
                    continue
                if min_val_nnums1 + min_val_nnums2 > tot:
                    result.append(0)
                    continue
                npairs = 0
                if len(nnums1) < len(nnums2):
                    for n, m in nnums1.items():
                        npairs += m * nnums2[tot - n]
                else:
                    for n, m in nnums2.items():
                        npairs += m * nnums1[tot - n]

                result.append(npairs)

        return result


def test():
    sol = Solution()

    cases = [
        (
            {
                "nums1": [1, 2],
                "nums2": [3, 4],
                "queries": [[2, 5], [1, 0, 0, 2], [2, 5]],
            },
            [2, 1],
        ),
        (
            {
                "nums1": [1, 1],
                "nums2": [2, 2, 3],
                "queries": [[2, 4], [1, 0, 1, 1], [2, 4]],
            },
            [2, 6],
        ),
        (
            {
                "nums1": [2, 5, 8, 4],
                "nums2": [1, 3, 8],
                "queries": [[2, 9], [1, 1, 2, 1], [2, 10]],
            },
            [1, 0],
        ),
        (
            {
                "nums1": [13, 4],
                "nums2": [1, 6, 2, 12, 2, 7, 13, 15],
                "queries": [[1, 2, 2, 26], [2, 17]],
            },
            [1],
        ),
    ]

    for i, (kwargs, expected) in enumerate(cases, 1):
        print(f"running test {i}")
        got = sol.numberOfPairs(**kwargs)
        assert got == expected, f"case {i} failed: got {got}, expected {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
