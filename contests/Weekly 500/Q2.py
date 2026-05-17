"""
Q2.
Event: Weekly Contest 500
Topic: Staff, Weekly Contest 500
Difficulty: Medium
Status: Solved
Date: 2026-05-02

Mistakes:
- Missing `p <= max_` in the sum over small primes. Edge case `n = 1`.
"""


class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        r = int(str(n)[::-1])
        max_ = max(r, n)
        min_ = min(r, n)

        sieve = set(
            2*k + 1
            for k in range(1, (max_ + 1)//2)
        )

        small_primes = set([2])

        p = 3
        while p**2 <= max_:
            p = min(sieve)
            sieve.discard(p)
            small_primes.add(p)
            for k in range(1, max_//p + 1):
                sieve.discard(p*k)

        result = sum(
            p
            for p in small_primes
            if (p >= min_ and p <= max_)
        )
        result += sum(
            p
            for p in sieve
            if (p >= min_ and p <= max_)
        )
        return result


def test():
    sol = Solution()

    cases = [
        (
            {"n": 13},
            132,
        ),
        (
            {"n": 10},
            17,
        ),
        (
            {"n": 8},
            0,
        ),
    ]

    for i, (kwargs, expected) in enumerate(cases, 1):
        print(f"running test {i}")
        got = sol.sumOfPrimesInRange(**kwargs)
        assert got == expected, f"case {i} failed: got {got}, expected {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
