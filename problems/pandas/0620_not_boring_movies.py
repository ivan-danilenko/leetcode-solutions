"""
620. Not Boring Movies
Topic: Database
Difficulty: Easy
Status: Solved
Date: 2026-04-01
"""

import pandas as pd


def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    mask = cinema["id"].mod(2).eq(1)
    mask &= cinema["description"].ne("boring")
    cinema = cinema.loc[mask].sort_values(by="rating", ascending=False)
    return cinema


def test():
    cases = [
        (
            pd.DataFrame(
                {
                    "id": [103, 104, 105, 106, 107],
                    "movie": ["movie1", "movie2", "movie3", "movie4", "movie5"],
                    "description": ["good", "OK", "boring", "very_good", "horrible"],
                    "rating": [1.0, 10.0, 6.0, 5.1, 7.5],
                }
            ),
            pd.DataFrame(
                {
                    "id": [107, 103],
                    "movie": ["movie5", "movie1"],
                    "description": ["horrible", "good"],
                    "rating": [7.5, 1.0],
                },
                index=[4, 0],
            ),
        ),
    ]

    for i, (database, expected) in enumerate(cases, 1):
        print(f"running test {i}")
        got = not_boring_movies(database)
        assert got.equals(
            expected
        ), f"case {i} failed: \n got\n {got},\n expected\n {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
