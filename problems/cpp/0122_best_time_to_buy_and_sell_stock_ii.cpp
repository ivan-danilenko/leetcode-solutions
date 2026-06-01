/*
122. Best Time to Buy and Sell Stock II
Topic: Array, Dynamic Programming, Greedy
Difficulty: Medium
Status: Solved
Date: 2026-06-01

Key idea:
- Sum over all increments.
*/

#include <vector>
#include <iostream>
using namespace std;

class Solution
{
public:
    int maxProfit(vector<int> &prices)
    {
        int profit = 0;
        for (size_t i = 1; i < prices.size(); ++i)
        {
            int diff = prices[i] - prices[i - 1];
            if (diff > 0)
            {
                profit += diff;
            }
        }

        return profit;
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
        int expected = 7;

        auto actual = sol.maxProfit(nums);
        expectEqual(actual, expected, "example 1");
    }

    {
        vector<int> nums = {1, 2, 3, 4, 5};
        int expected = 4;

        auto actual = sol.maxProfit(nums);
        expectEqual(actual, expected, "example 2");
    }

    {
        vector<int> nums = {7, 6, 4, 3, 1};
        int expected = 0;

        auto actual = sol.maxProfit(nums);
        expectEqual(actual, expected, "example 2");
    }

    return 0;
}