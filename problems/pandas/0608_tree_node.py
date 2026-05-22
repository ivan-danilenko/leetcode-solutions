"""
608. Tree Node
Topic: Database
Difficulty: Medium
Status: Solved
Date: 2026-05-22
"""

import pandas as pd
import numpy as np


def tree_node(tree: pd.DataFrame) -> pd.DataFrame:
    parents = set(tree["p_id"].dropna())

    tree["type"] = np.select(
        [tree["p_id"].isna(), tree["id"].isin(parents)],
        ["Root", "Inner"],
        default="Leaf",
    )

    return tree[["id", "type"]]


def test():
    cases = [
        (
            pd.DataFrame(
                [[1, None], [2, 1], [3, 1], [4, 2], [5, 2]], columns=["id", "p_id"]
            ).astype({"id": "Int64", "p_id": "Int64"}),
            pd.DataFrame(
                [[1, "Root"], [2, "Inner"], [3, "Leaf"], [4, "Leaf"], [5, "Leaf"]],
                columns=["id", "type"],
            ).astype({"id": "Int64", "type": "str"}),
        ),
    ]

    for i, (database, expected) in enumerate(cases, 1):
        print(f"running test {i}")
        got = tree_node(database)
        assert got.equals(
            expected
        ), f"case {i} failed: \n got\n {got},\n expected\n {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
