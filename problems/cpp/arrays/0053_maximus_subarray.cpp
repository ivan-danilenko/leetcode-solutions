/*
53. Maximum Subarray
Topic: Array, Divide and Conquer, Dynamic Programming
Difficulty: Medium
Status: Solved
Date: 2026-06-01

Key idea:
- Sliding window.
*/

#include <vector>
#include <iostream>
using namespace std;

class Solution
{
public:
    int maxSubArray(vector<int> &nums)
    {
        int max_sum = nums[0];
        int curr_sum = nums[0];

        for (size_t right = 1; right < nums.size(); ++right)
        {
            if (curr_sum > 0)
            {
                curr_sum += nums[right];
            }
            else
            {
                curr_sum = nums[right];
            }

            if (curr_sum > max_sum)
            {
                max_sum = curr_sum;
            }
        }

        return max_sum;
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
        vector<int> nums = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
        int expected = 6;

        auto actual = sol.maxSubArray(nums);
        expectEqual(actual, expected, "example 1");
    }

    {
        vector<int> nums = {1};
        int expected = 1;

        auto actual = sol.maxSubArray(nums);
        expectEqual(actual, expected, "example 2");
    }

    {
        vector<int> nums = {5, 4, -1, 7, 8};
        int expected = 23;

        auto actual = sol.maxSubArray(nums);
        expectEqual(actual, expected, "example 3");
    }

    return 0;
}