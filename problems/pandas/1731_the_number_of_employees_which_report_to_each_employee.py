"""
1731. The Number of Employees Which Report to Each Employee
Topic: Database
Difficulty: Easy
Status: Solved
Date: 2026-04-04
"""

import pandas as pd
import numpy as np


def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
    # to avoid coercion to float because of nulls
    employees["reports_to"] = employees["reports_to"].astype("Int64")

    grouped = employees.groupby("reports_to", as_index=False)
    result = grouped.agg(
        reports_count=("employee_id", "count"), average_age=("age", "mean")
    )

    result["average_age"] = np.floor(result["average_age"] + 0.5).astype("Int32")
    result.rename(columns={"reports_to": "employee_id"}, inplace=True)

    name_map = employees.set_index("employee_id")["name"]
    result["name"] = result["employee_id"].map(name_map)

    result = result[["employee_id", "name", "reports_count", "average_age"]]
    return result


def test():
    cases = [
        (
            pd.DataFrame(
                {
                    "employee_id": [9, 6, 4, 2],
                    "name": ["Hercy", "Alice", "Bob", "Winston"],
                    "reports_to": [None, 9, 9, None],
                    "age": [43, 41, 36, 37],
                }
            ),
            pd.DataFrame(
                {
                    "employee_id": [9],
                    "name": ["Hercy"],
                    "reports_count": [2],
                    "average_age": [39],
                },
            ),
        ),
        (
            pd.DataFrame(
                {
                    "employee_id": [1, 2, 3, 4, 5, 6, 7, 8],
                    "name": [
                        "Michael",
                        "Alice",
                        "Bob",
                        "Charlie",
                        "David",
                        "Eve",
                        "Frank",
                        "Grace",
                    ],
                    "reports_to": [None, 1, 1, 2, 2, 3, None, None],
                    "age": [45, 38, 42, 34, 40, 37, 50, 48],
                }
            ),
            pd.DataFrame(
                {
                    "employee_id": [1, 2, 3],
                    "name": ["Michael", "Alice", "Bob"],
                    "reports_count": [2, 2, 1],
                    "average_age": [40, 37, 37],
                }
            ),
        ),
    ]

    for i, (database, expected) in enumerate(cases, 1):
        print(f"running test {i}")
        got = count_employees(database)
        assert got.equals(
            expected
        ), f"case {i} failed: \n got\n {got},\n expected\n {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
