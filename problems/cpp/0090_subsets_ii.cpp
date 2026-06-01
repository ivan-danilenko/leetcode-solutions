/*
90. Subsets II
Topic: Array, Backtracking, Bit Manipulation
Difficulty: Medium
Status: Solved
Date: 2026-06-01

Key idea:
- Backtrack.
*/

#include <vector>
#include <string>
#include <iostream>
using namespace std;

class Solution
{
public:
    vector<vector<int>> subsetsWithDup(vector<int> &nums)
    {
        sort(nums.begin(), nums.end());
        vector<vector<int>> result = {{}};
        // may allocate too much, can `.shrink_to_fit` if needed
        result.reserve(1 << nums.size());

        unsigned size = 1;
        int multiplicity;
        for (int i = 0; i < (int)nums.size();)
        {
            multiplicity = 1;
            auto n = nums[i];
            i++;
            while (i < (int)nums.size() && nums[i] == n)
            {
                multiplicity++;
                i++;
            }
            for (unsigned j = 0; j < size; j++)
            {
                auto subset = result[j];
                for (auto m = 1; m < multiplicity + 1; m++)
                {
                    result.push_back(subset);
                    result.back().insert(result.back().end(), m, n);
                }
            }
            size *= multiplicity + 1;
        }
        return result;
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
void printNestedVector(const vector<T> &v)
{
    cout << "[";
    for (int i = 0; i < (int)v.size(); ++i)
    {
        if (i > 0)
            cout << ", ";
        printVector(v[i]);
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

template <typename T>
void sortMembers(
    vector<vector<T>> &v)
{
    for (auto &member : v)
    {
        sort(member.begin(), member.end());
    }
}

template <typename T>
void expectNestedVectorEqual(
    vector<vector<T>> &actual,
    vector<vector<T>> &expected,
    const string &testName,
    bool ignoreInternalOrder = false,
    bool ignoreExternalOrder = false)
{
    if (ignoreInternalOrder)
    {
        sortMembers(actual);
        sortMembers(expected);
    }
    if (sameVector(actual, expected, ignoreExternalOrder))
    {
        cout << "PASS: " << testName << "\n";
    }
    else
    {
        cout << "FAIL: " << testName << "\n";
        cout << "  expected: ";
        printNestedVector(expected);
        cout << "\n";
        cout << "  actual:   ";
        printNestedVector(actual);
        cout << "\n";
    }
}

// -------------------- Main --------------------

int main()
{
    Solution sol;

    {
        vector<int> nums = {1, 2, 3};
        vector<vector<int>> expected = {{}, {1}, {2}, {1, 2}, {3}, {1, 3}, {2, 3}, {1, 2, 3}};

        auto actual = sol.subsetsWithDup(nums);
        expectNestedVectorEqual(actual, expected, "example 1", true, true);
    }

    {
        vector<int> nums = {1, 2, 2};
        vector<vector<int>> expected = {{}, {1}, {1, 2}, {2}, {2, 2}, {1, 2, 2}};

        auto actual = sol.subsetsWithDup(nums);
        expectNestedVectorEqual(actual, expected, "example 2", true, true);
    }

    {
        vector<int> nums = {0};
        vector<vector<int>> expected = {{}, {0}};

        auto actual = sol.subsetsWithDup(nums);
        expectNestedVectorEqual(actual, expected, "example 3", true, true);
    }

    return 0;
}