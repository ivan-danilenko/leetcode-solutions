"""
Q2.
Event: Biweekly Contest 183
Topic: Staff, ??
Difficulty: Medium
Status: Solved
Date: 2026-05-23

Mistake:
- For `k=2` residues may match. *Distinct* residues.
"""

from collections import Counter


class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            return 0 if (nums[0] - nums[1]) % k != 0 else 1

        even_counter = Counter(nums[2 * a] % k for a in range((len(nums) + 1) // 2))
        odd_counter = Counter(nums[2 * a + 1] % k for a in range(len(nums) // 2))

        odd_mins = [
            sum(
                (
                    ((i - a) % k) * m
                    if 2 * ((i - a) % k) <= k
                    else (k - ((i - a) % k)) * m
                )
                for i, m in odd_counter.items()
            )
            for a in range(k)
        ]
        even_mins = [
            sum(
                (
                    ((i - a) % k) * m
                    if 2 * ((i - a) % k) <= k
                    else (k - ((i - a) % k)) * m
                )
                for i, m in even_counter.items()
            )
            for a in range(k)
        ]

        return min(
            odd_mins[i] + even_mins[j] for i in range(k) for j in range(k) if i != j
        )


def test():
    sol = Solution()

    cases = [
        (
            {"nums": [1, 1, 1], "k": 3},
            1,
        ),
        (
            {"nums": [1, 4, 2, 8], "k": 3},
            2,
        ),
        (
            {"nums": [1, 4], "k": 3},
            1,
        ),
        (
            {"nums": [1, 5], "k": 3},
            0,
        ),
    ]

    for i, (kwargs, expected) in enumerate(cases, 1):
        print(f"running test {i}")
        got = sol.minOperations(**kwargs)
        assert got == expected, f"case {i} failed: got {got}, expected {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
