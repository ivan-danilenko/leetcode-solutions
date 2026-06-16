"""
313. Super Ugly Number
Topic: Array, Math, Dynamic Programming
Difficulty: Medium
Status: Solved
Date: 2026-03-18

Key idea:
- every ugly number has a unique form `p*N` where `p` is a prime, `N` is ugly
  and all prime divisors of `N` are at most `p`.
- use heap to keep track of candidates for the next ugly number of form `p*N`
  as above, one for each prime `p`.

Mistakes:
- Doubles coming from numbers which have their highest prime with a multiplicity.
  Changed the rule to track lowest prime power.
- First implementation allowed several numbers with the same `p` in the heap,
  and it reduced speed.
"""

from typing import List
from heapq import heappushpop
from dataclasses import dataclass


@dataclass(slots=True, order=True, frozen=True)
class UglyNumber:
    r"""
    Every ugly number has form `p*N` where `p` is a prime, `N` is ugly
    and all prime divisors of `N` are at most `p`.
    `value` is the number itself,
    `largest_prime_index` is the index of `p` in `primes`
    `previous_ugly_number_index` is the index of `N` in `first_ugly_numbers`
    """

    value: int
    largest_prime_index: int
    previous_ugly_number_index: int


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        if n == 1:
            return 1

        first_ugly_numbers = [None] * (n - 1)
        first_ugly_numbers[0] = UglyNumber(
            value=1,
            largest_prime_index=-1,
            previous_ugly_number_index=-1,
        )

        # the first prime will be the next ugly number
        current_ugly_number = UglyNumber(
            value=primes[0],
            largest_prime_index=0,
            previous_ugly_number_index=0,
        )

        candidate_heap = [
            UglyNumber(
                value=primes[prime_index],
                largest_prime_index=prime_index,
                previous_ugly_number_index=0,
            )
            for prime_index in range(1, min(len(primes), n - 1))
        ]
        # primes are sorted, so no need to heapify

        for i in range(1, n - 1):
            first_ugly_numbers[i] = current_ugly_number

            prime_index = current_ugly_number.largest_prime_index
            # now we need a new candidate with largest prime
            # `primes[prime_index]`
            new_previous_ugly_number_index = next(
                j
                for j in range(
                    current_ugly_number.previous_ugly_number_index + 1, n - 1
                )
                if first_ugly_numbers[j].largest_prime_index <= prime_index
            )
            new_value = first_ugly_numbers[new_previous_ugly_number_index].value
            new_value *= primes[prime_index]
            current_ugly_number = heappushpop(
                candidate_heap,
                UglyNumber(
                    value=new_value,
                    largest_prime_index=prime_index,
                    previous_ugly_number_index=new_previous_ugly_number_index,
                ),
            )

        return current_ugly_number.value


def test():
    sol = Solution()

    cases = [
        (
            {"n": 12, "primes": [2, 7, 13, 19]},
            32,
        ),
        (
            {"n": 1, "primes": [2, 3, 5]},
            1,
        ),
        (
            {"n": 25, "primes": [3, 5, 7, 17, 19, 23, 29, 43, 47, 53]},
            81,
        ),
        (
            {"n": 40, "primes": [2, 3, 11, 13, 17, 23, 29, 31, 37, 47]},
            72,
        ),
        (
            {"n": 2, "primes": [2, 3, 5]},
            2,
        ),
        (
            {"n": 3, "primes": [2]},
            4,
        ),
    ]

    for i, (kwargs, expected) in enumerate(cases, 1):
        got = sol.nthSuperUglyNumber(**kwargs)
        assert got == expected, f"case {i} failed: got {got}, expected {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
