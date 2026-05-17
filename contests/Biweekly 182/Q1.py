"""
Q1.
Event: Biweekly Contest 182
Topic: Staff, ??
Difficulty: Easy
Status: Solved
Date: 2026-05-09
"""


class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        scores = {str(i): i for i in range(7)}
        scores["WD"] = 1
        scores["W"] = 0
        scores["NB"] = 1

        score = 0
        counter = 0
        for ev in events:
            if ev == "W":
                counter += 1
                if counter == 10:
                    break
            score += scores[ev]

        return [score, counter]


def test():
    sol = Solution()

    cases = [
        (
            {"events": ["1", "4", "W", "6", "WD"]},
            [12, 1],
        ),
        (
            {"events": ["WD", "NB", "0", "4", "4"]},
            [10, 0],
        ),
        (
            {"events": ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W"]},
            [0, 10],
        ),
    ]

    for i, (kwargs, expected) in enumerate(cases, 1):
        print(f"running test {i}")
        got = sol.scoreValidator(**kwargs)
        assert got == expected, f"case {i} failed: got {got}, expected {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
