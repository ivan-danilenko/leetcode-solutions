"""
Q1.
Event: Weekly Contest 503
Topic: Staff, Weekly Contest 503
Difficulty: Easy
Status: Solved
Date: 2026-05-23
"""


class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        def generator():
            nums_iter = iter(nums)
            last_val = next(nums_iter)
            counter = 1
            yield last_val
            for val in nums_iter:
                if val != last_val:
                    last_val = val
                    counter = 1
                else:
                    counter += 1
                if counter <= k:
                    yield val

        return list(generator())


def test():
    sol = Solution()

    cases = [
        (
            {"nums": [1, 1, 1, 2, 2, 3], "k": 2},
            [1, 1, 2, 2, 3],
        ),
        (
            {"nums": [1, 2, 3], "k": 1},
            [1, 2, 3],
        ),
    ]

    for i, (kwargs, expected) in enumerate(cases, 1):
        print(f"running test {i}")
        got = sol.limitOccurrences(**kwargs)
        assert got == expected, f"case {i} failed: got {got}, expected {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
