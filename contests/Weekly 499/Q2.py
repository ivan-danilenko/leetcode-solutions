"""
Q2.
Event: Weekly Contest 499
Topic: Staff, Weekly Contest 499
Difficulty: Medium
Status: Solved
Date: 2026-04-25
"""

from collections import Counter


class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = "aeiou"

        vowel_counter = Counter(
            ch for ch in s if ch in vowels
        )
        vowels_by_frequency = sorted(
            ((freq, -s.find(ch), ch) for ch, freq in vowel_counter.items()),
            reverse=True
        )
        vowel_sequence = "".join(ch * freq for freq, _, ch in vowels_by_frequency)

        result = ""
        vowels_used = 0
        for i in range(len(s)):
            if s[i] not in vowels:
                result += s[i]
            else:
                result += vowel_sequence[vowels_used]
                vowels_used += 1

        return result


def test():
    sol = Solution()

    cases = [
        (
            {"s": "leetcode"},
            "leetcedo",
        ),
        (
            {"s": "aeiaaioooa"},
            "aaaaoooiie",
        ),
        (
            {"s": "baeiou"},
            "baeiou",
        ),
    ]

    for i, (kwargs, expected) in enumerate(cases, 1):
        print(f"running test {i}")
        got = sol.sortVowels(**kwargs)
        assert got == expected, f"case {i} failed: got {got}, expected {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
