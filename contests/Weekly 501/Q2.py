"""
Q2.
Event: Weekly Contest 501
Topic: Staff, Weekly Contest 501
Difficulty: Medium
Status: Solved
Date: 2026-05-09
"""

import re
from collections import Counter


class Solution:
    def countWordOccurrences(self, chunks: list[str], queries: list[str]) -> list[int]:
        s = "".join(chunks)

        pattern = re.compile(r"[a-z]+(\-[a-z]+)*")
        count = Counter(x.group(0) for x in pattern.finditer(s))

        result = [count.get(que, 0) for que in queries]
        return result


def test():
    sol = Solution()

    cases = [
        (
            {"chunks": ["hello wor", "ld hello"], "queries": ["hello", "world", "wor"]},
            [2, 1, 0],
        ),
        (
            {"chunks": ["a--b a-", "-c"], "queries": ["a", "b", "c"]},
            [2, 1, 1],
        ),
        (
            {"chunks": ["hello"], "queries": ["hello", "ell"]},
            [1, 0],
        ),
        (
            {"chunks": ["m  cq-i "], "queries": ["m", "cq-i", "nm"]},
            [1, 1, 0],
        ),
    ]

    for i, (kwargs, expected) in enumerate(cases, 1):
        print(f"running test {i}")
        got = sol.countWordOccurrences(**kwargs)
        assert got == expected, f"case {i} failed: got {got}, expected {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
