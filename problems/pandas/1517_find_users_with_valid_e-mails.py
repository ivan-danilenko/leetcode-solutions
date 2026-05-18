"""
1517. Find Users With Valid E-Mails
Topic: Database
Difficulty: Easy
Status: Solved
Date: 2026-05-18
"""

import pandas as pd


def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    pattern = r"^[a-zA-Z]+[a-zA-Z0-9_.-]*@leetcode\.com$"
    valid_email_mask = users["mail"].str.match(pattern)

    return users[valid_email_mask]


def test():
    cases = [
        (
            pd.DataFrame(
                [
                    [1, "Winston", "winston@leetcode.com"],
                    [2, "Jonathan", "jonathanisgreat"],
                    [3, "Annabelle", "bella-@leetcode.com"],
                    [4, "Sally", "sally.come@leetcode.com"],
                    [5, "Marwan", "quarz#2020@leetcode.com"],
                    [6, "David", "david69@gmail.com"],
                    [7, "Shapiro", ".shapo@leetcode.com"],
                ],
                columns=["user_id", "name", "mail"],
            ).astype({"user_id": "int64", "name": "object", "mail": "object"}),
            pd.DataFrame(
                [
                    [1, "Winston", "winston@leetcode.com"],
                    [3, "Annabelle", "bella-@leetcode.com"],
                    [4, "Sally", "sally.come@leetcode.com"],
                ],
                index=[0, 2, 3],
                columns=["user_id", "name", "mail"],
            ).astype({"user_id": "int64", "name": "object", "mail": "object"}),
        ),
        (
            pd.DataFrame(
                [
                    [1, "Winston", "winston@leetcode?com"],
                ],
                columns=["user_id", "name", "mail"],
            ).astype({"user_id": "int64", "name": "object", "mail": "object"}),
            pd.DataFrame(
                columns=["user_id", "name", "mail"],
            ).astype({"user_id": "int64", "name": "object", "mail": "object"}),
        ),
    ]

    for i, (database, expected) in enumerate(cases, 1):
        print(f"running test {i}")
        got = valid_emails(database)
        assert got.equals(
            expected
        ), f"case {i} failed: \n got\n {got},\n expected\n {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
