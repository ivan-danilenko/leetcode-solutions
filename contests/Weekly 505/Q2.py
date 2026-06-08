"""
Q2.
Event: Weekly Contest 505
Topic: Staff, Weekly Contest 505
Difficulty: Medium
Status: ?
Date: 2026-06-06
"""


class Solution:
    def generateValidStrings(self, n: int, k: int) -> list[str]:

        def generate_strings(n, k):
            if n == 1:
                return [("0", 0), ("1", 0)]
            result = []
            for s, cost in generate_strings(n - 1, k):
                result.append((s + "0", cost))
                if cost <= k - n + 1 and s[-1] != "1":
                    result.append((s + "1", cost + n - 1))

            return result

        return [s for s, _ in generate_strings(n, k)]


def test():
    sol = Solution()

    cases = [
        (
            {"n": 3, "k": 1},
            ["000", "010", "100"],
        ),
        (
            {"n": 1, "k": 0},
            ["0", "1"],
        ),
    ]

    for i, (kwargs, expected) in enumerate(cases, 1):
        print(f"running test {i}")
        got = sol.generateValidStrings(**kwargs)
        assert sorted(got) == sorted(
            expected
        ), f"case {i} failed: got {got}, expected {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
