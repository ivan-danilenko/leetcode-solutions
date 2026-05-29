"""
Q2.
Event: Weekly Contest 503
Topic: Staff, Weekly Contest 503
Difficulty: Medium
Status: ?
Date: 2026-05-23
"""


class Solution:
    def passwordStrength(self, password: str) -> int:
        special_characters = "!@#$"
        characters = set(password)

        strength = 0
        for ch in characters:
            if ch.isalpha():
                strength += 1
                if ch.isupper():
                    strength += 1
            if ch.isnumeric():
                strength += 3
            if ch in special_characters:
                strength += 5

        return strength


def test():
    sol = Solution()

    cases = [
        (
            {"password": "aA1!"},
            11,
        ),
        (
            {"password": "bbB11#"},
            11,
        ),
    ]

    for i, (kwargs, expected) in enumerate(cases, 1):
        print(f"running test {i}")
        got = sol.passwordStrength(**kwargs)
        assert got == expected, f"case {i} failed: got {got}, expected {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
