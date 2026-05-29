/*
1. Two Sum
Topic: Junior, Array, Hash Table
Difficulty: Easy
Status: Solved
Date: 2026-05-28

Key idea:
- Keep previous numbers in a hashmap.
*/

#include <vector>
#include <unordered_map>
#include <string>
#include <iostream>
#include <exception>
using namespace std;

class Solution
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        unordered_map<int, int> needed_to_index = unordered_map<int, int>();
        for (int i = 0; i < nums.size(); i++)
        {
            if (needed_to_index.find(nums[i]) != needed_to_index.end())
            {
                vector<int> result = vector<int>(2);
                return {needed_to_index[nums[i]], i};
            }

            needed_to_index[target - nums[i]] = i;
        };

        throw runtime_error("Solution not found");
    };
};

// -------------------- Test helpers --------------------

template <typename T>
void printVector(const vector<T> &v)
{
    cout << "[";
    for (int i = 0; i < (int)v.size(); ++i)
    {
        if (i > 0)
            cout << ", ";
        cout << v[i];
    }
    cout << "]";
}

template <typename T>
bool sameVector(vector<T> a, vector<T> b, bool ignoreOrder = false)
{
    if (ignoreOrder)
    {
        sort(a.begin(), a.end());
        sort(b.begin(), b.end());
    }
    return a == b;
}

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

template <typename T>
void expectVectorEqual(
    const vector<T> &actual,
    const vector<T> &expected,
    const string &testName,
    bool ignoreOrder = false)
{
    if (sameVector(actual, expected, ignoreOrder))
    {
        cout << "PASS: " << testName << "\n";
    }
    else
    {
        cout << "FAIL: " << testName << "\n";
        cout << "  expected: ";
        printVector(expected);
        cout << "\n";
        cout << "  actual:   ";
        printVector(actual);
        cout << "\n";
    }
}

// -------------------- Main --------------------

int main()
{
    Solution sol;

    {
        vector<int> nums = {2, 7, 11, 15};
        int target = 9;
        vector<int> expected = {0, 1};

        auto actual = sol.twoSum(nums, target);
        expectVectorEqual(actual, expected, "example 1");
    }

    {
        vector<int> nums = {3, 2, 4};
        int target = 6;
        vector<int> expected = {1, 2};

        auto actual = sol.twoSum(nums, target);
        expectVectorEqual(actual, expected, "example 2");
    }

    {
        vector<int> nums = {3, 3};
        int target = 6;
        vector<int> expected = {0, 1};

        auto actual = sol.twoSum(nums, target);
        expectVectorEqual(actual, expected, "example 3");
    }

    return 0;
}