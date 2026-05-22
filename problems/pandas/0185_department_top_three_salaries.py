"""
185. Department Top Three Salaries
Topic: Database
Difficulty: Hard
Status: Solved
Date: 2026-05-22

Possible changes:
- Replace mapping with merge. It's a more SQL-like and generalizable
  [e.g. if more than one column is needed] solution. Here mapping
  is a more natural choice.
"""

import pandas as pd


def top_three_salaries(
    employee: pd.DataFrame, department: pd.DataFrame
) -> pd.DataFrame:
    top_salaries = employee.assign(
        rank=employee.groupby("departmentId")["salary"].rank(
            method="dense",
            ascending=False,
        )
    )
    top_salaries = top_salaries[top_salaries["rank"] <= 3].copy()

    mapping = department.set_index("id")["name"]
    top_salaries["Department"] = top_salaries["departmentId"].map(mapping)

    top_salaries.rename(
        columns={
            "name": "Employee",
            "salary": "Salary",
        },
        inplace=True,
    )
    top_salaries = top_salaries[["Department", "Employee", "Salary"]]
    return top_salaries


def test():
    cases = [
        (
            {
                "employee": pd.DataFrame(
                    [
                        [1, "Joe", 85000, 1],
                        [2, "Henry", 80000, 2],
                        [3, "Sam", 60000, 2],
                        [4, "Max", 90000, 1],
                        [5, "Janet", 69000, 1],
                        [6, "Randy", 85000, 1],
                        [7, "Will", 70000, 1],
                    ],
                    columns=["id", "name", "salary", "departmentId"],
                ).astype(
                    {
                        "id": "Int64",
                        "name": "object",
                        "salary": "Int64",
                        "departmentId": "Int64",
                    }
                ),
                "department": pd.DataFrame(
                    [
                        [1, "IT"],
                        [2, "Sales"],
                    ],
                    columns=["id", "name"],
                ).astype({"id": "Int64", "name": "object"}),
            },
            pd.DataFrame(
                [
                    ["IT", "Joe", 85000],
                    ["Sales", "Henry", 80000],
                    ["Sales", "Sam", 60000],
                    ["IT", "Max", 90000],
                    ["IT", "Randy", 85000],
                    ["IT", "Will", 70000],
                ],
                columns=["Department", "Employee", "Salary"],
            ).astype(
                {
                    "Department": "str",
                    "Employee": "object",
                    "Salary": "Int64",
                }
            ),
        ),
    ]

    for i, (databases, expected) in enumerate(cases, 1):
        print(f"running test {i}")
        got = top_three_salaries(**databases)
        try:
            pd.testing.assert_frame_equal(
                got.reset_index(drop=True),
                expected.reset_index(drop=True),
                check_like=True,
            )
        except AssertionError as ex:
            raise AssertionError(f"case {i} failed:" + "\n" + str(ex))

    print("all tests passed")


if __name__ == "__main__":
    test()
