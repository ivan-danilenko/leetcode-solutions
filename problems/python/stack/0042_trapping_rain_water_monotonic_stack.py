"""
42. Trapping Rain Water
Topic: Array, Two Pointers, Dynamic Programming, Stack, Monotonic Stack
Difficulty: Hard
Status: Solved
Date: 2026-05-19

Key idea:
- Using monotonic stack to record of the shape on the left
"""

from typing import List
from collections import deque


class Solution:
    def trap(self, height: List[int]) -> int:
        left_profile = deque([[height[0], None]])

        water_volume = 0
        for i in range(1, len(height)):
            if left_profile and height[i] < left_profile[-1][0]:
                left_profile.append([height[i], i])
                continue

            while left_profile and height[i] > left_profile[-1][0]:
                l_height, l_position = left_profile.pop()
                if l_position is not None:
                    depth = min(left_profile[-1][0], height[i]) - l_height
                    water_volume += (i - l_position) * depth

            if not left_profile or height[i] != left_profile[-1][0]:
                left_profile.append([height[i], l_position])

        return water_volume


def test():
    sol = Solution()

    cases = [
        (
            {"height": [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]},
            6,
        ),
        (
            {"height": [0, 1, 0, 2, 1, 0, 0, 1, 1, 3, 2, 1, 2, 1]},
            9,
        ),
        (
            {"height": [4, 2, 0, 3, 2, 5]},
            9,
        ),
    ]

    for i, (kwargs, expected) in enumerate(cases, 1):
        print(f"running test {i}")
        got = sol.trap(**kwargs)
        assert got == expected, f"case {i} failed: got {got}, expected {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
