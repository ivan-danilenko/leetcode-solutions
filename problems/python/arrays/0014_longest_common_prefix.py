"""
14. Longest Common Prefix
Topic: Array, String, Trie
Difficulty: Easy
Status: Solved
Date: 2026-03-17

Key idea:
Use zip to look at letters on the same position.

Mistakes:
None
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_common_prefix = ""
        for chars in zip(*strs):
            # at each step we extract characters on the same position
            if len(set(chars)) > 1:
                break

            # if all characters are equal, we append this character
            longest_common_prefix += chars[0]

        return longest_common_prefix


def test():
    sol = Solution()

    cases = [
        ((["flower", "flow", "flight"],), "fl"),
        ((["dog", "racecar", "car"],), ""),
    ]

    for i, (args, expected) in enumerate(cases, 1):
        got = sol.longestCommonPrefix(*args)
        assert got == expected, f"case {i} failed: got {got}, expected {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
