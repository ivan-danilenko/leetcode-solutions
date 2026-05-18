"""
1731. Number of Unique Subjects Taught by Each Teacher
Topic: Database
Difficulty: Easy
Status: Solved
Date: 2026-05-18
"""

import pandas as pd


def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    result = teacher.groupby("teacher_id", as_index=False)
    result = result.nunique("subject_id")
    result.rename(columns={"subject_id": "cnt"}, inplace=True)
    result = result[["teacher_id", "cnt"]]

    return result


def test():
    cases = [
        (
            pd.DataFrame(
                [
                    [1, 2, 3],
                    [1, 2, 4],
                    [1, 3, 3],
                    [2, 1, 1],
                    [2, 2, 1],
                    [2, 3, 1],
                    [2, 4, 1],
                ],
                columns=["teacher_id", "subject_id", "dept_id"],
            ).astype(
                {"teacher_id": "Int64", "subject_id": "Int64", "dept_id": "Int64"}
            ),
            pd.DataFrame(
                [
                    [1, 2],
                    [2, 4],
                ],
                columns=["teacher_id", "cnt"],
            ).astype({"teacher_id": "Int64", "cnt": "int64"}),
        ),
    ]

    for i, (database, expected) in enumerate(cases, 1):
        print(f"running test {i}")
        got = count_unique_subjects(database)
        assert got.equals(
            expected
        ), f"case {i} failed: \n got\n {got},\n expected\n {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
