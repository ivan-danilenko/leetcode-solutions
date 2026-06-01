/*
121. Best Time to Buy and Sell Stock
Topic: Array, Dynamic Programming
Difficulty: Easy
Status: Solved
Date: 2026-06-01

Key idea:
- Keep record of lowest price seen.
*/

#include <vector>
#include <iostream>
using namespace std;

class Solution
{
public:
    int maxProfit(vector<int> &prices)
    {
        int curr_min = prices[0];
        int max_profit = 0;
        int curr_profit;
        for (auto p : prices)
        {
            curr_profit = p - curr_min;
            if (curr_profit > max_profit)
            {
                max_profit = curr_profit;
            }
            else if (p < curr_min)
            {
                curr_min = p;
            }
        }

        return max_profit;
    }
};

// -------------------- Test helpers --------------------

template <typename T>
void expectEqual(const T &actual, const T &expected, const string &testName)
{
    if (actual == expected)
    {
        cout << "PASS: " << testName << "\n";
    }
    else
    {
        cout << "FAIL: " << testName << "\n";
        cout << "  expected: " << expected << "\n";
        cout << "  actual:   " << actual << "\n";
    }
}

// -------------------- Main --------------------

int main()
{
    Solution sol;

    {
        vector<int> nums = {7, 1, 5, 3, 6, 4};
        int expected = 5;

        auto actual = sol.maxProfit(nums);
        expectEqual(actual, expected, "example 1");
    }

    {
        vector<int> nums = {7, 6, 4, 3, 1};
        int expected = 0;

        auto actual = sol.maxProfit(nums);
        expectEqual(actual, expected, "example 2");
    }

    return 0;
}