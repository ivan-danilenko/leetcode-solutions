/*
167. Two Sum II - Input Array Is Sorted
Topic: Array, Two Pointers, Binary Search
Difficulty: Medium
Status: Solved
Date: 2026-05-28

Key idea:
- Two pointers.

Mistakes:
- Array is 1-indexed, not 0-indexed
*/

#include <vector>
#include <string>
#include <iostream>
#include <exception>
using namespace std;

class Solution
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        int left = 0, right = nums.size() - 1;
        while (left < right)
        {
            int sum = nums[left] + nums[right];
            if (sum == target)
                // array is 1-indexed
                return {left + 1, right + 1};

            if (sum > target)
                right--;
            else
                left ++;
        }

        throw runtime_error("Solution not found");
    }
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
        vector<int> expected = {1, 2};

        auto actual = sol.twoSum(nums, target);
        expectVectorEqual(actual, expected, "example 1");
    }

    {
        vector<int> nums = {2, 3, 4};
        int target = 6;
        vector<int> expected = {1, 3};

        auto actual = sol.twoSum(nums, target);
        expectVectorEqual(actual, expected, "example 2");
    }

    {
        vector<int> nums = {-1, 0};
        int target = -1;
        vector<int> expected = {1, 2};

        auto actual = sol.twoSum(nums, target);
        expectVectorEqual(actual, expected, "example 3");
    }

    return 0;
}