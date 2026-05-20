"""
42. Trapping Rain Water
Topic: Array, Two Pointers, Dynamic Programming, Stack, Monotonic Stack
Difficulty: Hard
Status: Solved
Date: 2026-05-19

Key idea:
- Keep track of the level of water from the lower side.
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_left, max_right = height[left], height[right]
        water_volume = 0

        while left < right:
            if max_left < max_right:
                left += 1
                if height[left] > max_left:
                    max_left = height[left]
                else:
                    water_volume += max_left - height[left]
            else:
                right -= 1
                if height[right] > max_right:
                    max_right = height[right]
                else:
                    water_volume += max_right - height[right]
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
