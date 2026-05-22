"""
1393. Capital Gain/Loss
Topic: Database
Difficulty: Medium
Status: Solved
Date: 2026-05-22
"""

import pandas as pd


def capital_gainloss(stocks: pd.DataFrame) -> pd.DataFrame:
    signed_prices = stocks.assign(
        capital_gain_loss=stocks["price"].where(
            stocks["operation"] == "Sell",
            -stocks["price"],
        )
    )
    gain_loss = signed_prices.groupby("stock_name", as_index=False)[
        "capital_gain_loss"
    ].sum()

    return gain_loss


def test():
    cases = [
        (
            pd.DataFrame(
                [
                    ["Leetcode", "Buy", 1, 1000],
                    ["Corona Masks", "Buy", 2, 10],
                    ["Leetcode", "Sell", 5, 9000],
                    ["Handbags", "Buy", 17, 30000],
                    ["Corona Masks", "Sell", 3, 1010],
                    ["Corona Masks", "Buy", 4, 1000],
                    ["Corona Masks", "Sell", 5, 500],
                    ["Corona Masks", "Buy", 6, 1000],
                    ["Handbags", "Sell", 29, 7000],
                    ["Corona Masks", "Sell", 10, 10000],
                ],
                columns=["stock_name", "operation", "operation_day", "price"],
            ).astype(
                {
                    "stock_name": "object",
                    "operation": "object",
                    "operation_day": "Int64",
                    "price": "Int64",
                }
            ),
            pd.DataFrame(
                [
                    ["Corona Masks", 9500],
                    ["Handbags", -23000],
                    ["Leetcode", 8000],
                ],
                columns=["stock_name", "capital_gain_loss"],
            ).astype(
                {
                    "stock_name": "str",
                    "capital_gain_loss": "Int64",
                }
            ),
        ),
    ]

    for i, (database, expected) in enumerate(cases, 1):
        print(f"running test {i}")
        got = capital_gainloss(database)
        assert got.equals(
            expected
        ), f"case {i} failed: \n got\n {got},\n expected\n {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
